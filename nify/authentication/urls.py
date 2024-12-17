# urls.py
from django.urls import path, include
from authentication import views
from authentication.views import profile_view

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("verify_otp/", views.verify_otp, name="verify_otp"),
    path("accounts/profile/", profile_view, name="profile"),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.logout_view, name='logout'),
]
