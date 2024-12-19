from django.urls import path
from home import views



urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('404', views.PAGE_NOT_FOUND, name = '404'),
    path('contact',views.contact, name='contact'),
    path('project_detail', views.project_detail, name='project_detail'),
    path('panel', views.panel, name='panel'),
    path('view_detail/<slug:slug>/', views.view_detail, name='view_detail'),
    
]
