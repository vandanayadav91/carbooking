from django.contrib import admin
from car_admin.models import Service,Blog,Vehicle,Review,Booking,Numbering,centalProcess

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
    list_display3=('review_images','review_title','review_icon','review_desc')
admin.site.register(Review,reviewAdmin)

class bookingAdmin(admin.ModelAdmin):
    list_display4=('booking_icon','booking_title','review_desc')
admin.site.register(Booking,bookingAdmin)


class numberingAdmin(admin.ModelAdmin):
    list_display5=('num_icon','num_counter','num_title')
admin.site.register(Numbering,numberingAdmin)

class centalProcessAdmin(admin.ModelAdmin):
    list_display6=('pro_title','pro_desc','pro_number')
admin.site.register(centalProcess,centalProcessAdmin)


# Register your models here.
