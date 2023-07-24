from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel

# Create your views here.

def home(request):
	data = StudentModel.objects.all()
	return render(request,"home.html",{"data":data})

def create(request):
	if request.method=="POST":
		data = StudentForm(request.POST)
		if data.is_valid():
			data.save()
			msg="record created"
			fm = StudentForm()
			return render(request,"create.html",{"fm":fm,"msg":msg})
		else:
			msg=data
			fm = StudentForm()
			return render(request,"create.html",{"fm":data})
	else:
		fm = StudentForm()
		return render(request,"create.html",{"fm":fm})


def remove(request,id):
	st=StudentModel.objects.get(rno=id)
	st.delete()
	return redirect("home")

