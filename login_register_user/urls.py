from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/login/authenticate/', views.login_create, name='login_create'),
    path('auth/register/', views.register_user, name='register'),
    path('auth/register/validation/', views.register_user_validation, name='register_validation'),
    path('auth/logout/', views.logout_user, name='logout')
]

