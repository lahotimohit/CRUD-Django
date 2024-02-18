from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def student_tmp(request):
    return render(request, 'students/student.html')


def create(request):
    form = forms.stuform
    if request.method == "POST":
        form = forms.stuform(request.POST)
        if form.is_valid():
            form.save();
    return render(request, 'students/create.html', {'form':form})

def roll(request):
    if request.method == "POST":
        id = request.POST.get('rollno')
        return redirect(update, roll=id)
    return render(request, 'students/roll.html')


def update(request, roll):
    student = models.student.objects.get(id=roll)
    if request.method=='POST':
        form = forms.stuform(request.POST, instance=student)
        if form.is_valid():
            form.save()
            print("Code reach here...")
            return redirect(student_tmp)
        else:
            print(form.errors)
    return render(request, 'students/update.html', {'data':student})

def roll1(request):
    if request.method == "POST":
        id = request.POST.get('rollno')
        return redirect(show, roll=id)
    return render(request, 'students/roll.html')

def show(request, roll):
    student = models.student.objects.get(id=roll)
    return render(request, 'students/show.html', {'data':student})

def roll2(request):
    if request.method == "POST":
        id = request.POST.get('rollno')
        return redirect(delete, roll=id)
    return render(request, 'students/roll.html')

def delete(request, roll):
    student = models.student.objects.get(id=roll)
    if request.method == "POST":
        student.delete()
        return redirect('/', roll=id)
    return render(request, 'students/delete.html', {'data':student})