from django.shortcuts import render
from django.http import HttpResponse
from . import forms

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
            # request.session['name'] = form.cleaned_data['name']
            # request.session['address'] = form.cleaned_data['address']
            # request.session['course'] = form.cleaned_data['course']
            # request.session['phone_number'] = form.cleaned_data['phone_number'] 
            form.save();
    return render(request, 'students/create.html', {'form':form})
