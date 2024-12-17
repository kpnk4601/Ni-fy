from django.shortcuts import render, redirect
from .models import ContactForm
from django.contrib import messages
from home.models import Categories, Courses
from django.http import JsonResponse

# Create your views here.
def index(request):
    category = Categories.objects.all().order_by('id')[0:3]
    course = Courses.objects.filter(status = 'PUBLISH').order_by('-id')

    context = {
        'category': category,
        'course': course,
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):  
    if request.method == "POST":  
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        # Create and save a new contact instance
        contact_instance = ContactForm(name=name, email=email, subject = subject, message=message)
        print(contact_instance)
        contact_instance.save()
        
        messages.success(request, "Your message has been sent successfully!")  # Add success message
        return redirect('contact')  # Redirect to the index page after submission
        
    return render(request, "contact.html")



def view_detail(request):
    return render(request, 'view_detail.html')




def project_detail(request):
    category = Categories.get_all()
    course = Courses.get_all_course()

    context = {
        'course': course,
        'category': category,
    }
    return render(request, 'project_detail.html', context)


def view_detail(request, slug):
    course = Courses.objects.filter(slug = slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    
    context = {
        'course': course,
    }

    
    return render(request, 'view_detail.html', context)


def PAGE_NOT_FOUND(request):
    return render(request, 'error/404.html')





def admin_upload(request):
    return render(request, 'admin-upload.html')


