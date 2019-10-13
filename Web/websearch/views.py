from django.shortcuts import render
from django.contrib import messages
from django import forms
from django.forms import widgets
from django.http import HttpResponse
import json 
# Create your views here.

def vtable(request):
    return render(request, 'websearch/table.html')