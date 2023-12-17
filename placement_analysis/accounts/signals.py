
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from accounts.models import CollegeModel, CompanyModel


# Inside your signal handlers

@receiver(post_save, sender=User)
def create_college_model(sender, instance, created, **kwargs):
    if created and instance.groups.filter(name='college').exists():
        print(f"Creating CollegeModel for user: {instance.username}")


@receiver(post_save, sender=User)
def create_company_model(sender, instance, created, **kwargs):
    if created and instance.groups.filter(name='company').exists():
        print(f"Creating CompanyModel for user: {instance.username}")
