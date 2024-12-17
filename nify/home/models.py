
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

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
class Courses(models.Model):
    STATUS = (
        ('PUBLISH', 'PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    
    feature_image = models.ImageField(upload_to='Media/feature_image', null=True)
    feature_video = models.CharField(max_length=300, null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, default=0)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, null=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('view_detail', kwargs={'slug':self.slug})


    
    @classmethod
    def get_all_course(self):
        return Courses.objects.filter(status = 'PUBLISH').order_by('-id')
    
# for automatic slug creating

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Courses.objects.filter(slug=slug). order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
        

def pre_save_post_receiver(sender, instance,  *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Courses)


    