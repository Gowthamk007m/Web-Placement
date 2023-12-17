from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('userpage/', user_home, name='user_home'),
    path('user/dashboard/', user_dashboard, name='user_dashboard'),
    path('upload_resume/', upload_resume, name='upload_resume'),

    path('apply_for_job/<int:job_id>/', apply_for_job, name='apply_for_job'),
    path('jobslist', joblist, name='jobslist'),


    path('login', login_view, name='login'),
    path('register/',register, name='register'),
    path('logout/',LogoutUser, name='logout'),

]
