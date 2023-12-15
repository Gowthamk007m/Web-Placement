from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.


def main_page(request):
    return render(request, 'admin_main/adminhome.html')
