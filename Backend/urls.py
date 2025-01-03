from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('works/', views.works, name='works'),
    path('projects/<int:id>/<str:name>/', views.projects, name='projects'),
]
