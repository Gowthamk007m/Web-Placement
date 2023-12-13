from django.db import models
from django.contrib.auth.models import User


class AllUsers(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)



class Jobs(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()  # Fixed the missing field name
    company = models.CharField(max_length=50)
    salary = models.PositiveIntegerField(null=True, blank=True)
    vacancy = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed')])

    def __str__(self):
        return self.job_title


class UserModel(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    is_approved = models.BooleanField(default=False)
    applied_jobs = models.ForeignKey(Jobs, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.profile.username


class CollegeModel(models.Model):
    college = models.OneToOneField(User, on_delete=models.CASCADE)


class CompanyModel(models.Model):
    company = models.OneToOneField(User, on_delete=models.CASCADE)


class PlacementRequests(models.Model):
    college = models.ForeignKey(CollegeModel, related_name="college_requests", on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyModel, related_name="company_requests", on_delete=models.CASCADE)
    description = models.TextField()  
    request_status = models.BooleanField(default=False)
    request_date = models.DateField(auto_now_add=True)
    