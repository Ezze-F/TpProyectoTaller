from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def index(request):
    # Vista principal
    return render(request, 'inicio/index.html')
