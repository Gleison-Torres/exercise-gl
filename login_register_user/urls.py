from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_user, name='login'),
    path('login/authenticate/', views.login_create, name='login_create'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout')
]

