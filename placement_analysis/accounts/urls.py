from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('userpage/', user_home, name='user_home'),

    path('login', login_view, name='login'),
    path('register/',register, name='register'),
    path('logout/',LogoutUser, name='logout'),

]
