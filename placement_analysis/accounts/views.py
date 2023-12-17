from .forms import JobApplicationForm
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ResumeUploadForm
from .models import UserModel
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import UserModel, Jobs
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def main_page(request):
    return render(request, 'home/index2.html')


def user_home(request):
    data=Jobs.objects.all()
    return render(request, 'user/userhome.html',{'data':data})


def user_dashboard(request):
    # Get the current user
    user_profile = UserModel.objects.get(profile=request.user)

    # Get relevant data for the dashboard
    applied_jobs = user_profile.applied_jobs.all()
    # Adjust this based on your business logic
    placement_drives = Jobs.objects.filter(status='open')
    part_time_job_openings = Jobs.objects.filter(
        status='open', company__isnull=False)

    context = {
        'user_profile': user_profile,
        'applied_jobs': applied_jobs,
        'placement_drives': placement_drives,
        'part_time_job_openings': part_time_job_openings,
    }

    return render(request, 'user_dashboard.html', context)


# views.py


def upload_resume(request):
    user_profile = UserModel.objects.get(profile=request.user)

    if request.method == 'POST':
        form = ResumeUploadForm(
            request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Resume uploaded successfully!")
            # Replace with the URL you want to redirect to
            return redirect('user_home')
    else:
        form = ResumeUploadForm(instance=user_profile)

    context = {
        'form': form,
    }

    return render(request, 'user/upload.html', context)


# views.py


def joblist(request):
    job = Jobs.objects.all()

    context = {
        'job': job,
    }

    return render(request, 'user/joblist.html', context)


def apply_for_job(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = UserModel.objects.get(profile=request.user)
            user_profile.applied_jobs = job
            user_profile.resume = form.cleaned_data['resume']
            user_profile.save()

            # Replace with the URL you want to redirect to after job application
            return redirect('user_dashboard')
    else:
        form = JobApplicationForm()

    context = {
        'form': form,
        'job': job,
    }

    return render(request, 'apply_for_job.html', context)



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_type = request.POST.get('user_type')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username, email=email, password=password1)

        # Assign user to the selected group based on user type
        if user_type == 'company':
            group_name = 'company'
        elif user_type == 'college':
            group_name = 'college'
        elif user_type == 'admin':
            group_name = 'admin'
        else:
            group_name = 'user'

        group = Group.objects.get(name=group_name)
        user.groups.add(group)

        user.save()

        if user_type == 'college':
            CollegeModel.objects.create(college=user)
        elif user_type == 'company':
            CompanyModel.objects.create(company=user)


        messages.success(request, "Account created successfully")
        return redirect('login')
    else:
        return render(request, 'home/reg.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.groups.filter(name='user').exists():
                return redirect('user_home')

            elif user.groups.filter(name='college').exists():
                return redirect('college_dashboard')

            elif user.groups.filter(name='admin').exists():
                return redirect('admin_home')

            elif user.groups.filter(name='company').exists():
                return redirect('companies_home')
        else:
            error_message = 'Invalid ID or password'
            return render(request, 'home/Login1.html', {'error_message': error_message})

    # Return the login page template for GET requests
    return render(request, 'home/Login1.html')


def LogoutUser(request):
    logout(request)
    return redirect('login')
