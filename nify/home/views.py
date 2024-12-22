from django.shortcuts import render, redirect,  get_object_or_404
from .models import ContactForm
from django.contrib import messages
from home.models import Categories, Project
from django.contrib.auth.decorators import login_required

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
        'search_query': search_query,
    }
    return render(request, 'project_detail.html', context)






def view_detail(request, slug):
    categories = Categories.objects.all()
    projects = Project.objects.filter(slug = slug)
    
    if projects.exists():
        projects = projects.first()
    else:
        return redirect('404')
    
    context = {
        'project': projects,
        'categories': categories,
        
    }

    
    return render(request, 'view_detail.html', context)


def PAGE_NOT_FOUND(request):
    return render(request, 'error/404.html')




@login_required
def panel(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        feature_image = request.FILES.get('feature_image', None)
        feature_video = request.POST.get('feature_video')
        categorie_id = request.POST.get('categorie')
        categorie = get_object_or_404(Categories, id=categorie_id)

        Project.objects.create(
            user=request.user,
            title=title,
            description=description,
            feature_image=feature_image,
            feature_video=feature_video,
            categorie=categorie,
        )
        messages.success(request, "Project uploaded successfully.")
        return redirect('recent')

    categories = Categories.get_all()
    return render(request, 'panel.html', {'categories': categories})

   
@login_required
def recent(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'recent.html', {'projects': projects}) 
