from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Intern(models.Model):
	comp_name = models.CharField(max_length=30)
	job = models.CharField(max_length=30)
	desc = models.CharField(max_length=100)
	def __str__(self):
		return self.comp_name

class Signup1(models.Model):
	full_name = models.CharField(max_length=30)
	gender = models.CharField(max_length=10)
	phone_no = models.IntegerField()
	status = models.CharField(max_length=30,default="Pending")
	email= models.EmailField()
	internship=models.ForeignKey(Intern,on_delete=models.CASCADE)
	resume_file = models.FileField(upload_to='resume_folder')
	class Meta:
		unique_together=["full_name","email","internship"]
	def __str__(self):
		return self.full_name


