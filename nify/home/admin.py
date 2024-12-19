from django.contrib import admin
from home.models import Project, Categories, Author, Requirements, Installnation

# Inline classes
class Installnation_TabularInline(admin.TabularInline):  # Fixed typo
    model = Installnation  # Correctly reference the model
    extra = 1

class Requirements_TabularInline(admin.TabularInline):
    model = Requirements  # Correctly reference the model

# ModelAdmin for Project
class ProjectAdmin(admin.ModelAdmin):  # Follow Django naming conventions
    inlines = [Installnation_TabularInline, Requirements_TabularInline]

# Register your models
admin.site.register(Project, ProjectAdmin)  
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Requirements)
admin.site.register(Installnation)  
