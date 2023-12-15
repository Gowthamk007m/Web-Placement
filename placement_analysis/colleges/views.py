from accounts.models import UserModel
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .forms import PlacementRequestForm
from accounts.models import CollegeModel, PlacementRequests, UserModel
from django.contrib import messages
from accounts.models import *
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.models import Group

# Create your views here.


def main_page(request):
    return render(request, 'colleges/collegehome.html')


def college_dashboard(request):
    college_profile = CollegeModel.objects.get(college=request.user)

    # Retrieve placement requests for the college
    placement_requests = PlacementRequests.objects.filter(
        college=college_profile)

    # Retrieve users associated with the college
    college_users = UserModel.objects.filter(profile__groups__name='college')

    context = {
        'college_profile': college_profile,
        'placement_requests': placement_requests,
        'college_users': college_users,
    }

    return render(request, 'colleges/collegehome.html', context)

def getcompany(request):
    company=CompanyModel.objects.all()
    return render(request,'colleges/companies.html',{'company':company})


def get_users_in_students_group(request):
    # Assuming 'students' is the name of the group
    students_group = Group.objects.get(name='user')

    # Retrieve users in the 'students' group
    students = UserModel.objects.filter(profile__groups=students_group)

    return render(request, 'colleges/userlist.html', {'students': students})


# views.py


def download_pdf(request, user_id):
    user = get_object_or_404(UserModel, id=user_id)

    # Your logic to generate a PDF for the user
    # ...

    # Example: Returning a simple HttpResponse for demonstration purposes
    response = HttpResponse("PDF content", content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{user.profile.username}_resume.pdf"'
    return response


def send_placement_request(request):
    college_profile = CollegeModel.objects.get(college=request.user)

    if request.method == 'POST':
        form = PlacementRequestForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data['description']
            company = form.cleaned_data['company']


            # Create a placement request
            PlacementRequests.objects.create(
                college=college_profile, company=company, description=description, request_status=False)

            messages.success(request, "Placement request sent successfully!")
            return redirect('college_dashboard')
    else:
        form = PlacementRequestForm()

    context = {
        'form': form,
    }

    return render(request, 'colleges/send_placement_request.html', context)


def manage_user_module(request, user_id):
    # Implement your logic for managing the user module
    # You may want to approve/reject user accounts here
    # Update the UserModel instances as needed

    # Example: Assuming UserModel has an is_approved field
    user_profile = UserModel.objects.get(id=user_id)
    user_profile.is_approved = True  # Set to False for rejection
    user_profile.save()

    messages.success(request, "User account approved/rejected successfully!")
    return redirect('college_dashboard')

# def approve(request,pk):
#     applicant = UserModel.objects.filter(profile_id=pk)

#     if request.method == 'POST':
#         form = PlacementRequestForm(request.POST)
    

def approve_request(request, request_id):
    # Get the leave request object from the database
    user = UserModel.objects.get(id=request_id)

    # Check if the user is authorized to approve or deny this request
    # if not request.user.is_staff:
    #     return redirect('home')

    # Handle the form submission
    if request.method == 'POST':
        # Get the approval status from the form data
        is_approved = request.POST.get('is_approved')

        if is_approved == 'approved':
            # Update the leave request object with the new approval status
            user.is_approved = True
            user.is_denied = False

   
            user.save()

            # Redirect the user back to the detail page of the leave request
            return redirect('userlist')
        elif is_approved == 'denied':
            # Update the leave request object with the new approval status
            user.is_approved = False
            user.is_denied = True

            user.save()

            # Send a message to the student
            messages.warning(request, 'Your leave request has been denied.')

            # Redirect the user back to the detail page of the leave request
            return redirect('userlist')

    # Render the form for the warden to approve or deny the request
    return render(request, 'colleges/approve.html', {'request': user})
