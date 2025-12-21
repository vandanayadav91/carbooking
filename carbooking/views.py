from django.http import HttpResponse
from django.shortcuts import render
from car_admin.models import Service,Vehicle,Blog,Numbering,centalProcess



# def HomePage(request):
#     return HttpResponse("Hello welcome to home page")

# def AboutPage(request):
#     return HttpResponse("Hello welcome to about page")

# def BlogPage(request):
#     return HttpResponse("Hello welcome to blog page")

# def ServicePage(request):
#     return HttpResponse("Hello welcome to service page")



def HomePage(request):
    serviceData=Service.objects.all()
    vehicleData=Vehicle.objects.all()
    blogData=Blog.objects.all()
    NumberingData=Numbering.objects.all()
    centalProcessData=centalProcess.objects.all()
    data={
        'service_show':serviceData,
        'vehicle_show':vehicleData,
        'blog_show':blogData,
        'num_show':NumberingData,
        'centalProcess_show':centalProcessData,
    }

    return render(request,"index.html",data)

def AboutPage(request):
    
    return render(request,"About.html")

def BlogPage(request):
    NumberingData=Numbering.objects.all()
    centalProcessData=centalProcess.objects.all()
    data={
        'num_show':NumberingData,
        'centalProcess_show':centalProcessData,
    }
    return render(request,"Blog.html",data)

def contactPage(request):
    return render(request,"Contact.html")

def ServicePage(request):
    serviceData=Service.objects.all()
    data={
        'service_show':serviceData,
    }
    return render(request,"Service.html",data)


def featurepage(request):
    return render(request,"feature.html")

def carpage(request):
    return render(request,"car.html")


def teampage(request):
    return render(request,"team.html")

def testimonialpage(request):
    return render(request,"testimonial.html")

def numpages(request):
    return render(request,"numpages.html")




