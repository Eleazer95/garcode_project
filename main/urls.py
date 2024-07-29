from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact_view, name='contact'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('about/', views.about, name='about'),
]
