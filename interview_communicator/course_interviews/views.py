from django.shortcuts import render
from .models import Student

def index(request):
    return render(request, "index.html", locals())
