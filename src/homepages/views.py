from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'homepages/index.html')

def transport_intern(request):
    return render(request,'homepages/intern.html')

def transport_adr(request):
    return render(request,'homepages/adr.html')

def transport_frigorific(request):
    return render(request,'homepages/frigorific.html')

