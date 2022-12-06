from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name='home'),
    path('add/', views.addquestionpage, name='add'),
    path('add/addingQuestion/', views.addingquestionpage, name = 'adding'),
]