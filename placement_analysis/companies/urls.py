from django.urls import path
from .views import *

urlpatterns = [
    path('company', main_page, name='companies_home'),
    path('create_job/', create_job, name='create_job'),
     path('company_jobs/', view_company_jobs, name='company_jobs'),
    path('change_job_status/<int:job_id>/', change_job_status, name='change_job_status'),
]
