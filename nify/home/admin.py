from django.contrib import admin
from .models import ContactForm, Courses , Categories, Author

# Register your models here.
admin.site.register(Courses)
admin.site.register(Categories)
admin.site.register(Author)