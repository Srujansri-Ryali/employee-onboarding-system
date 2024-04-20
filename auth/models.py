from django.db import models


# Create your models here.
class Employee(models.Model):
    empNo = models.CharField(max_length=10)
    empName = models.CharField(max_length=50)
    empPosition = models.CharField(max_length=50)
    empUserName = models.CharField(max_length=20)
    empUserPassword = models.CharField(max_length=12)
    companyName = models.CharField(max_length=50)


CHOICES = (
    ('0', 'Default Application Form'),
    ('1', 'Customise Application Form')
)


class JobModel(models.Model):
    companyName = models.CharField(max_length=50)
    jobName = models.CharField(max_length=50)
    jobLocation = models.TextField(max_length=50)
    jobDescription = models.TextField(max_length=500)
    experienceRequired = models.CharField(max_length=10)
    skillsRequired = models.TextField(max_length=100)
    defaultApplicationForm = models.CharField(choices=CHOICES, max_length=2)
