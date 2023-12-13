from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def main_page(request):
    return render(request, 'home/index2.html')


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

            elif user.groups.filter(name='colleges').exists():
                return redirect('colleges_home')

            elif user.groups.filter(name='admin_main').exists():
                return redirect('admin_home')

            elif user.groups.filter(name='companies').exists():
                return redirect('companies_home')
        else:
            error_message = 'Invalid ID or password'
            return render(request, 'home/Login1.html', {'error_message': error_message})

    # Return the login page template for GET requests
    return render(request, 'home/Login1.html')


def LogoutUser(request):
    logout(request)
    return redirect('login')
