from django.contrib import admin
from .models import ContactForm, Project , Categories, Author

# Register your models here.
admin.site.register(Project)
admin.site.register(Categories)
admin.site.register(Author)