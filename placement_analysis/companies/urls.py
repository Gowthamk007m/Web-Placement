from django.urls import path
from . import views

urlpatterns = [
    path('company', views.main_page, name='companies_home'),
]
