
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.urls import reverse

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    SUBJECT_CHOICES = [
        ('1', 'General Inquiry'),
        ('2', 'Technical Support'),
        ('3', 'Business Proposal'),
    ]
    subject = models.CharField(max_length=1, choices=SUBJECT_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"


    




class Categories(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('-id')
    

class Author(models.Model):
    author_profile = models.ImageField(upload_to="media/author")
    name = models.CharField(max_length = 100, null=True)
    about_author = models.TextField()


    def __str__(self):
        return self.name
    



class Project(models.Model):
    STATUS = (
        ('PUBLISH', 'PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    
    feature_image = models.ImageField(upload_to='Media/feature_image', null=True)
    feature_video = models.CharField(max_length=300, null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False, default=1)
    description = models.TextField()
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, null=True)



    class Meta:
        db_table = 'home_project'

    @classmethod
    def get_all_project(self):
        return Project.objects.filter(status = 'PUBLISH').order_by('-id')
        

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Return the absolute URL for the project detail page
        return reverse('view_detail', kwargs={'slug': self.slug})



    

    
# for automatic slug creating

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Project.objects.filter(slug=slug). order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
        

def pre_save_post_receiver(sender, instance,  *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Project)


class Requirements(models.Model):
    project = models.ForeignKey(Project,related_name='requirements', on_delete=models.CASCADE, default=1)
    points = models.CharField(max_length=500)

    def __str__(self):
        return self.points

class Installnation(models.Model):
    project = models.ForeignKey(Project, related_name='installnation',on_delete=models.CASCADE, default=1)
    Text = models.TextField(max_length=1000)