from django.urls import path
from home import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('facilities/', views.facilities, name='facilities'),
    path('academic-details/', views.academic, name='academic'),
    path('admission-details/', views.admission, name='admission'),
    path('glimpses/', views.glimpses, name='glimpses'),
    path('about-school/', views.about, name='about'),
    path('principal-message/', views.principal, name='principal'),
    path('administrator-message/', views.administrator, name='administrator'),
    path('president-message/', views.president, name='president'),
]
