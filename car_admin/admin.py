from django.contrib import admin
from car_admin.models import Service,Blog,Vehicle,Review,Booking,Numbering,centalProcess,HeroForm,contactsform

class ServiceAdmin(admin.ModelAdmin):
    list_display1=('ser_icon','ser_title','ser_desc')
admin.site.register(Service,ServiceAdmin)



class blogAdmin(admin.ModelAdmin):
    list_display2=('blog_images','blog_date','blog_comment','blog_author','blog_title','blog_desc')
admin.site.register(Blog,blogAdmin)


class vehicleAdmin(admin.ModelAdmin):
    list_display3=('vehicle_images','vehicle_title','vehicle_rate')
admin.site.register(Vehicle,vehicleAdmin)


class reviewAdmin(admin.ModelAdmin):
    list_display4=('review_images','review_title','review_icon','review_desc')
admin.site.register(Review,reviewAdmin)

class bookingAdmin(admin.ModelAdmin):
    list_display5=('booking_icon','booking_title','review_desc')
admin.site.register(Booking,bookingAdmin)


class numberingAdmin(admin.ModelAdmin):
    list_display6=('num_icon','num_counter','num_title')
admin.site.register(Numbering,numberingAdmin)

class centalProcessAdmin(admin.ModelAdmin):
    list_display7=('pro_title','pro_desc','pro_number')
admin.site.register(centalProcess,centalProcessAdmin)

class HeroFormAdmin(admin.ModelAdmin):
    list_display8=('car_type','pickup_location','drop_location','pickup_date','pickup_time','drop_date','drop_time')
admin.site.register(HeroForm,HeroFormAdmin)


class contactsformAdmin(admin.ModelAdmin):
    list_display9=('your_name','email','your_phone','your_projects','subjects','msg')
admin.site.register(contactsform,contactsformAdmin)





# Register your models here.
