from django import forms
from .models import JobModel
from django.forms import TextInput, Textarea


class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ['companyName', 'jobName', 'jobLocation', 'jobDescription', 'experienceRequired', 'skillsRequired', 'defaultApplicationForm']
        labels = {
            "companyName": "Company Name    ",
            "jobName": "Job Title   ",
            "jobLocation": "Job Location(s) ",
            "jobDescription": "Job Description  ",
            "experienceRequired": "Experience Required  ",
            "skillsRequired": "Skills Required  ",
            "defaultApplicationForm": "Type of application form "


        }
        widgets = {
            'companyName': TextInput(attrs={
                'class': "logininput",
                'placeholder': 'Freshworks'
            }),
            'jobName': TextInput(attrs={
                'class': "logininput",
                'placeholder': 'Developer'
            }),
            'jobLocation': Textarea(attrs={
                'class': "logininput",
                'placeholder': 'Chennai'
            }),
            'jobDescription': Textarea(attrs={
                'class': "logininput",
                'placeholder': 'JD'
            }),
            'skillsRequired': Textarea(attrs={
                'class': "logininput",
                'placeholder': 'HTML, CSS, JS'
            }),
            'experienceRequired': TextInput(attrs={
                'class': "logininput",
                'placeholder': '2+ years'
            }),

        }
