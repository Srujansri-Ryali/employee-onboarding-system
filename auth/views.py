from django.shortcuts import render
from .models import Employee, JobModel
from .forms import JobForm


def login(request):
    flag = 0
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        list_emp = Employee.objects.all()
        for emp in list_emp:
            if emp.empUserName == uname:
                if emp.empUserPassword == pwd:
                    flag = 0
                    print("Successfully Logged In")
                    return home(request, emp)
                else:
                    raise Exception("WRONG PASSWORD")
            else:
                flag = 1
            if flag == 1:
                raise Exception("USERNAME NOT FOUND")
    return render(request, 'login.html')


def home(request, emp):
    return render(request, 'home.html', {'user': emp})


def openjob(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORM SAVED")
            return render(request, 'postedsuccess.html', {'Job': JobModel.objects.last()})
        else:
            raise Exception("FORM VALIDATION FAILED")
            print("VALIDATION FAILED")
            print(form.errors)
    else:
        return render(request, 'postopenjob.html', {'form': JobForm()})


def job(request):
    return render(request, 'job.html', {'job': JobModel.objects.last()})


def viewJob(request):
    return render(request, 'viewjob.html', {'job': JobModel.objects.all()})
