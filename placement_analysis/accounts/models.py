from django.db import models
from django.contrib.auth.models import User


class Jobs(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
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
    applied_jobs = models.ForeignKey(
        Jobs, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.profile.username

