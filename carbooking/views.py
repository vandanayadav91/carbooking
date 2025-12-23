from django.http import HttpResponse
from django.shortcuts import render,redirect
from car_admin.models import Service,Vehicle,Blog,Numbering,centalProcess,HeroForm,contactsform



# def HomePage(request):
#     return HttpResponse("Hello welcome to home page")

# def AboutPage(request):
#     return HttpResponse("Hello welcome to about page")

# def BlogPage(request):
#     return HttpResponse("Hello welcome to blog page")

# def ServicePage(request):
#     return HttpResponse("Hello welcome to service page")



def HomePage(request):
    if request.method == "POST":
     HeroForm.objects.create(
            car_type=request.POST.get('car_type'),
            pickup_location=request.POST.get('pickup_location'),
            drop_location=request.POST.get('drop_location'),
            pickup_date=request.POST.get('pickup_date'),
            pickup_time=request.POST.get('pickup_time'),
            drop_date=request.POST.get('drop_date'),
            drop_time=request.POST.get('drop_time'),
     )
     return redirect('sucess')
    
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
    if request.method == "POST":
     contactsform.objects.create(
            your_name=request.POST.get('your_name'),
            email=request.POST.get('email'),
            your_phone=request.POST.get('your_phone'),
            your_projects=request.POST.get('your_projects'),
            subjects=request.POST.get('subjects'),
            msg=request.POST.get('msg'),
            
     )
     return redirect('contact')

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

def sucess(request):
    return render(request,"sucess.html")






