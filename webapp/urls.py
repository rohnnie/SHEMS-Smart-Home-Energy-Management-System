from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name='dashboard-index'),
    path("bla/", views.index, name='bla')

]

# Create your views here.
