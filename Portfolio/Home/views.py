from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutUs.html')

def experience(request):
    return render(request, 'experience.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'Conatctus.html')