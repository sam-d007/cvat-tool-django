from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.

def vw_index(request):
    return render(request, "vatic/index.html")