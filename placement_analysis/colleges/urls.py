from django.urls import path
from .views import *

urlpatterns = [
    # path('college', main_page, name='colleges_home'),
    path('college/dashboard/', college_dashboard, name='college_dashboard'),

    path('college/list/', getcompany, name='getcompany'),
    path('college/userlist/', get_users_in_students_group, name='userlist'),

    path('approve_request/<str:request_id>',approve_request, name='approve_request'),

    path('download_pdf/<int:user_id>/', download_pdf, name='download_pdf'),

    path('college/send_placement_request',send_placement_request, name='send_placement_request'),
    path('college/manage_user_module/<int:user_id>/',manage_user_module, name='manage_user_module'),
]
