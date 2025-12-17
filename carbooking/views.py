from django.http import HttpResponse
from django.shortcuts import render

# def HomePage(request):
#     return HttpResponse("Hello welcome to home page")

# def AboutPage(request):
#     return HttpResponse("Hello welcome to about page")

# def BlogPage(request):
#     return HttpResponse("Hello welcome to blog page")

# def ServicePage(request):
#     return HttpResponse("Hello welcome to service page")



def HomePage(request):
    return render(request,"index.html")

def AboutPage(request):
    return render(request,"About.html")

def BlogPage(request):
    return render(request,"Blog.html")

def contactPage(request):
    return render(request,"Contact.html")

def ServicePage(request):
    return render(request,"Service.html")




