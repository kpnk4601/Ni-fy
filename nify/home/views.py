from django.shortcuts import render, redirect
from .models import ContactForm
from django.contrib import messages
from home.models import Categories, Project

# Create your views here.
def index(request):
    category = Categories.objects.all().order_by('id')[0:3]
    projects = Project.objects.filter(status = 'PUBLISH').order_by('-id')

    context = {
        'category': category,
        'projects': projects,
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
    categories = Categories.objects.all()
    projects = Project.objects.all()

    # Get the search query from the GET parameters
    search_query = request.GET.get('search_query', '')

    # If there's a search query, filter the projects
    if search_query:
        projects = projects.filter(title__icontains=search_query)

    context = {
        'projects': projects,
        'categories': categories,
    }
    return render(request, 'project_detail.html', context)






def view_detail(request, slug):
    projects = Project.objects.filter(slug = slug)
    if projects.exists():
        projects = projects.first()
    else:
        return redirect('404')
    
    context = {
        'project': projects,
    }

    
    return render(request, 'view_detail.html', context)


def PAGE_NOT_FOUND(request):
    return render(request, 'error/404.html')





def admin_upload(request):
    return render(request, 'admin-upload.html')


