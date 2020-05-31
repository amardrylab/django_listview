from django.shortcuts import render
from .models import Student
from django.views.generic import ListView

# Create your views here.

class StudentView(ListView):
    model=Student
    template_name='student_list.html'
