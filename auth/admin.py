from django.contrib import admin
from auth.models import Employee, JobModel


class EmployeeAdmin(admin.ModelAdmin):
    emp_details = ['empNo', 'empName', 'empPosition', 'empUserName', 'empUserPassword']
    admin.site.register(Employee)

class JobAdmin(admin.ModelAdmin):
    emp_details = ['companyName', 'jobName', 'jobLocation', 'jobDescription', 'experienceRequired', 'skillsRequired']
    admin.site.register(JobModel)
