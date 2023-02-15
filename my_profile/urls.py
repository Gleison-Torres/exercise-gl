from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_profile, name='profile'),
    path('address/', views.my_address, name='address'),
    path('address/add-address', views.add_address, name='add-address'),
    path('address/add-address/get-cep', views.get_cep, name='get_cep'),
    path('info/', views.my_info, name='info')
]

