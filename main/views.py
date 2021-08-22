from django.shortcuts import render

# Create your views here.

def showmain(request):
    return render(request,'main.html')

def showmovie(request):
    return render(request,'movie.html')