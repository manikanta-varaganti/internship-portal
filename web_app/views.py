from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup1
from .models import Intern
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import tablib
# Create your views here.
@login_required
def home(request):
    if request.user.username == "hod":
        context=Signup1.objects.all()
        return render(request,'web_app/home.html',{'context':context})
    else:
        user=request.user.get_full_name()
        context=Signup1.objects.all().filter(full_name=user)
        return render(request,'web_app/home.html',{'context':context})

@login_required
def homepage(request):
    context=Intern.objects.all()
    return render(request,'web_app/homepage.html',{'context':context})

@login_required
def application(request):
    return render(request,'web_app/application.html')

def apphome(request):
    return render(request,'web_app/apphome.html')

@login_required
def createpost(request):
    full_name = request.POST["full_name"]
    if full_name==request.user.get_full_name():
        gender = request.POST["gender"]
        phone_no = request.POST["phone_no"]
        email_id= request.POST["email_id"]
        internship_id= request.POST["internship_id"]
        resume_file=request.FILES["resume_file"]    
        post = Signup1(full_name=full_name,gender=gender,phone_no=phone_no,email=email_id,internship_id=internship_id,resume_file=resume_file)
        messages.success(request, f'Applied for the internship succesfully')
        post.save()
        return render(request,'web_app/applied.html')
    else:
        messages.warning(request, f'Full name does not match')
        return render(request,'web_app/application.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def export_excel(request):
    headers = ('Student Name', 'Gender','Email Id','Phone No','Company Name','Job Profile')
    data = []
    data = tablib.Dataset(*data, headers=headers) 
    entries = Signup1.objects.all().filter(status="Accepted")
    for entry in entries:
        data.append((entry.full_name,entry.gender,entry.email,entry.phone_no,entry.internship.comp_name,entry.internship.job))
    response = HttpResponse(data.xls, content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = "attachment; filename=export.xls"
    return response