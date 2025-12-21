"""
URL configuration for carbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage, name="home"),

    
    path('about/',views.AboutPage, name="about"),
    path('blog/',views.BlogPage, name="blog"),
    path('contact/',views.contactPage, name="contact"),
    path('service/',views.ServicePage, name="service"),

    path('feature/',views.featurepage, name="feature"),
    path('car/',views.carpage, name="car"),
    path('team/',views.teampage, name="team"),
    path('testimonial/',views.testimonialpage, name="testimonial"),
    path('numpages/',views.numpages, name="numpages"),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)