from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'secondapp/home.html',context)


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'secondapp/add_student.html', {'form': form})
@login_required
def edit_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'secondapp/edit_student.html', {'form': form})

@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')