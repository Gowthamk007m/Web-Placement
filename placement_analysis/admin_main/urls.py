from django.urls import path
from . import views

urlpatterns = [
    path('adminpage', views.main_page, name='admin_home'),
]
