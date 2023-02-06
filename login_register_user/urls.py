from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('login/authenticate/', views.login_create, name='login_create'),
    path('register/', views.register_user, name='register'),
    path('register/validation/', views.register_user_validation, name='register_validation'),
    path('logout/', views.logout_user, name='logout')
]

