from django.shortcuts import render, redirect  
from myapp.forms import EmployeeForm  
from myapp.models import Employee

def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request,'add.html',{'form':form})

def index(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
   
def edit(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    return render(request,'edit.html', {'employee':employee, 'form': form})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, request.FILES, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'employee': employee, 'form': form})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")

def announcements(request):
    announcements = [
        {'title': 'Announcement 1', 'content': 'This is the content of announcement 1'},
    ]
    context = {
        'announcements': announcements
    }
    return render(request, 'announcements.html', context)
