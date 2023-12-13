from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.LogoutUser, name='logout'),

]
