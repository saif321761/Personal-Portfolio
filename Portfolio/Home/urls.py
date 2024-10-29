# Home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # example home view
    path('aboutUs', views.about, name="aboutUs"),
    path('contacUs/', views.contact, name="contacUs"),
    path('experience', views.experience, name="experience"),
    path('projects', views.project, name='projects')
]
