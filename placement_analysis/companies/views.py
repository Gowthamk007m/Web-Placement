from django.shortcuts import get_object_or_404, redirect
from accounts.models import *
from .forms import JobCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.


def main_page(request):
    return render(request, 'companies/companyhome.html')


# views.py


def create_job(request):
    if request.method == 'POST':
        form = JobCreationForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            # Replace with the URL you want to redirect to after job creation
            return redirect('companies_home')
    else:
        form = JobCreationForm()

    return render(request, 'companies/createjob.html', {'form': form})


# views.py


def view_company_jobs(request):
    company_jobs = Jobs.objects.filter(created_by=request.user)

# Get the count of job applicants for each job
    job_counts = {job.id: UserModel.objects.filter(applied_jobs=job).count() for job in company_jobs}

    context = {
        'company_jobs': company_jobs,
        'job_counts': job_counts,
    }
        
    return render(request, 'companies/company_jobs.html', context)


# views.py


def change_job_status(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)

    # Toggle the job status
    job.status = 'closed' if job.status == 'open' else 'open'
    job.save()

    return redirect('company_jobs')  # Redirect back to the company jobs view
