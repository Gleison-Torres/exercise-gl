from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_profile, name='profile'),
    path('address/', views.my_address, name='address'),
    path('address/add-address/', views.add_address, name='add_address'),
    path('address/<int:pk>/delete/', views.delete_address, name='delete_address'),
    path('address/<int:pk>/edit/', views.edit_address, name='edit_address'),
    path('info/', views.my_info, name='info'),
    path('info/profile/<int:pk>/edit/', views.edit_profile, name='edit_profile'),
    path('info/profile/password/', views.change_password, name='change_password'),
]

