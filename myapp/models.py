from django.db import models

# Create your models here.
class course(models.Model):
	course_name=models.CharField(max_length=25)
	course_instructor=models.CharField(max_length=25)
	course_duration=models.CharField(max_length=3)

	def __str__(self):
		return self.course_name

class source(models.Model):
	source_name=models.CharField(max_length=25)

	def __str__(self):
		return self.source_name

class lead_status(models.Model):
	lead_status=models.CharField(max_length=25)

	def __str__(self):
		return self.lead_status

class registration(models.Model):
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=25)
	mobile=models.CharField(max_length=10)
	email=models.CharField(max_length=30)
	date=models.DateField(null=True)
	course=models.CharField(max_length=25)
	source=models.CharField(max_length=25)
	lead_status=models.CharField(max_length=25)
	counselor=models.CharField(max_length=25)
	remarks=models.CharField(max_length=25)

	def __str__(self):
		return self.first_name

class calling(models.Model):
	calling=models.CharField(max_length=25)

	def __str__(self):
		return self.calling

class joining(models.Model):
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=25)
	course=models.CharField(max_length=25)
	date=models.DateField(null=True)
	course_fee=models.CharField(max_length=7)
	instructor=models.CharField(max_length=20)
	aadhar=models.CharField(max_length=12)
	mobile=models.CharField(max_length=10)
	email=models.CharField(max_length=30)
	remarks=models.CharField(max_length=25)
	status=models.CharField(max_length=25)

	def __str__(self):
		return self.first_name