from django.urls import path
from . import views

urlpatterns = [
    path('college', views.main_page, name='colleges_home'),
]
