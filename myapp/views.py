from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib.auth import authenticate,logout,login
from django.core.mail import send_mail
from lead_tracker import settings
#to activate the mail service provide the username and password in the email_credentails.py file 
# Create your views here.
def home(request):
	return render(request,'home_page.html')

def Course(request):
	c=course.objects.all()
	return render(request,'course.html',{"course":c})

def student_registration(request):
	c=course.objects.all()
	s=source.objects.all()
	l=lead_status.objects.all()
	if request.method=="POST":
		registration.objects.create(first_name=request.POST['First_Name'],last_name=request.POST['Last_Name'],mobile=request.POST['Mobile_Number'],email=request.POST['Email_Id'],date=request.POST['DATE'],course=request.POST['COURSE'],source=request.POST['SOURCE'],lead_status=request.POST['LEAD STATUS'],counselor=request.POST['COUNSELOR'],remarks=request.POST['REMARKS'])
		#send_mail("registration sucess!","Thanks for registering in digital lync .",settings.EMAIL_HOST_USER,[request.POST['Email_Id']],fail_silently=False)

		return HttpResponse("Data saved sucessfully and mail has been sent")
	return render(request,'student_registration_form.html',{"course":c,"source":s,"lead_status":l})

def walkins(request):
	r=registration.objects.all()
	return render(request,'walkins.html',{"walkins":r})

def Callings(request):
	c=lead_status.objects.all()
	if request.method=="POST":
		r=registration.objects.filter(lead_status=request.POST['demo call'],date=request.POST['DATE'] )
		return render(request,'calling_result.html',{"calling_results":r})
	return render(request,'callings.html',{"callings":c})

def counselling(request):
	c=course.objects.all()
	if request.method=="POST":
		r=registration.objects.filter(course=request.POST['counselling'],date=request.POST['DATE'] )
		return render(request,'counselling_result.html',{"counselling_result":r})
	return render(request,'counselling.html',{"course":c})

def Joining(request,pk):
	c=course.objects.all()
	if request.method=="POST":
		x=joining.objects.create(first_name=request.POST['First_Name'],last_name=request.POST['Last_Name'],course=request.POST['COURSE'],date=request.POST['DATE'],course_fee=request.POST['course_fee'],instructor=request.POST['instructor'],aadhar=request.POST['aadhar'],mobile=request.POST['Mobile_Number'],email=request.POST['Email_Id'],remarks=request.POST['REMARKS'],status=request.POST['status'])
		#send_mail("joining sucess!","Thanks for joining in digital lync .",settings.EMAIL_HOST_USER,[request.POST['Email_Id']],fail_silently=False)
		return redirect("current_status",x.id)
	return render(request,'joining.html',{"course":c})

def calling_result(request):
	print("hello")

def counselling_result(request):
	if request.method=="POST":
		return HttpResponse("dead")
	print("hello")

def Source(request):
	s=source.objects.all()
	return render(request,'source.html',{"source":s})

def Student(request):
	x=joining.objects.filter(status="completed")
	y=joining.objects.filter(status="delay")
	z=joining.objects.filter(status="ongoing")
	return render(request,'students.html',{"completed":x,"ongoing":z,"delay":y})

def Login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("home")
	
		else:
			return HttpResponse("credentials wrong")
			
			
	return render(request,"login.html")

def Logout(request):
    logout(request)
    return redirect("login")

def current_status(request,pk):
	x=joining.objects.filter(id=pk)
	if request.method=="POST":
		x=joining.objects.get(id=pk)
		status_data = request.POST['status1']
		x.status=status_data
		x.save()
		return redirect('student')
	return render(request,"current_status.html",{"current_status":x})

def dead(request,pk):
	x=registration.objects.get(id=pk)
	x.delete()
	return redirect("home")

def join(request):
	return redirect("joining")

def willing(request):
	return HttpResponse("willing")

def walkinsupdate(request,pk):
	c=course.objects.all()
	s=source.objects.all()
	l=lead_status.objects.all()
	x=registration.objects.get(id=pk)
	if request.method=="POST":
		x=registration.objects.get(id=pk)
		x.first_name=request.POST['First_Name']
		x.last_name=request.POST['Last_Name']
		x.mobile=request.POST['Mobile_Number']
		x.email=request.POST['Email_Id']
		x.course=request.POST['COURSE']
		x.source=request.POST['SOURCE']
		x.lead_status=request.POST['LEAD STATUS']
		x.counselor=request.POST['COUNSELOR']
		x.remarks=request.POST['REMARKS']
		x.save()
		#send_mail("details update notice!","your details has been updated sucessfully .",settings.EMAIL_HOST_USER,[request.POST['Email_Id']],fail_silently=False)
		return redirect("walkins")
	return render(request,"walkins_update.html",{"data":x,"course":c,"source":s,"lead_status":l})

def walkinsdelete(request,pk):
	x=registration.objects.get(id=pk)
	x.delete()
	return redirect("walkins")

def studentdelete(request,pk):
	x=joining.objects.get(id=pk)
	x.delete()
	return redirect("student")

def studentupdate(request,pk):
	c=course.objects.all()
	x=joining.objects.get(id=pk)
	if request.method=="POST":
		x=joining.objects.get(id=pk)
		x.first_name=request.POST['First_Name']
		x.last_name=request.POST['Last_Name']
		x.course=request.POST['COURSE']
		x.course_fee=request.POST['course_fee']
		x.instructor=request.POST['instructor']
		x.aadhar=request.POST['aadhar']
		x.mobile=request.POST['Mobile_Number']
		x.email=request.POST['Email_Id']
		x.remarks=request.POST['REMARKS']
		x.status=request.POST['status']
		x.save()
		#send_mail("details update notice!","your details has been updated sucessfully .",settings.EMAIL_HOST_USER,[request.POST['Email_Id']],fail_silently=False)
		return redirect("student")
	return render(request,"student_upadte.html",{"data":x,"course":c})
