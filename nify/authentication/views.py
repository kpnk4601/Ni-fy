from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from .models import OTP
from django.contrib.auth import logout
# Create your views here.

@login_required
def profile_view(request):
    return render(request, 'account/index.html')



def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'signup.html')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'signup.html')
            
            # Create new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False  # Deactivate user until OTP verification
            user.save()

            # Generate OTP
            otp = OTP.objects.create(user=user)
            otp.generate_otp()

            # Send OTP email
            subject = 'Verify Your Email'
            message = f'Your OTP for verification is: {otp.otp_code}\nThis code will expire in 5 minutes.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )

            # Store user ID in session
            request.session['temp_user_id'] = user.id
            
            messages.success(request, 'Registration successful! Please verify your email.')
            return redirect('verify_otp')

        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'signup.html')

    return render(request, 'signup.html')


def verify_otp(request):
    user_id = request.session.get('temp_user_id')
    if not user_id:
        messages.error(request, 'Please sign up first')
        return redirect('signup')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        
        try:
            user = User.objects.get(id=user_id)
            otp_obj = OTP.objects.filter(user=user).latest('created_at')

            if otp_obj.is_expired():
                messages.error(request, 'OTP has expired. Please request a new one.')
                return redirect('signup')

            if entered_otp == otp_obj.otp_code:
                user.is_active = True
                user.save()
                otp_obj.is_verified = True
                otp_obj.save()
                
                # Log the user in
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                
                # Clear the session
                if 'temp_user_id' in request.session:
                    del request.session['temp_user_id']
                
                messages.success(request, 'Email verified successfully! You are now logged in.')
                return redirect('login')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')

        except (User.DoesNotExist, OTP.DoesNotExist):
            messages.error(request, 'Invalid verification attempt')
            return redirect('signup')

    return render(request, 'otp.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("/")  # Redirect to home after login
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    
    return render(request, "login.html")


def logout_view(request):
    logout(request)  # Logs out the user and clears the session
    return redirect('login') 