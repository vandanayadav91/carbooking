from django.db import models

class Service(models.Model):
    ser_icon=models.CharField(max_length=200)
    ser_title=models.CharField(max_length=200)
    ser_desc=models.TextField()
# Create your models here.




# Create your models here numbering.

class Numbering(models.Model):
    num_icon=models.CharField(max_length=200)
    num_counter=models.CharField(max_length=200)
    num_title=models.CharField(max_length=200)




    # Create your models here cental process.

class centalProcess(models.Model):
    pro_title=models.TextField(max_length=200)
    pro_desc=models.TextField()
    pro_number=models.CharField(max_length=200)




#     # Create your models here cental feature.2

# class CentalFeature(models.Model):
#     feature_title=models.TextField(max_length=200)
#     feature_desc=models.TextField()
#     feature_icon=models.CharField(max_length=200)






     # Create your models here cental blog & news.

class Blog(models.Model):
    blog_image=models.ImageField(upload_to='media/',blank=True,default='images/car-4.png',null=True)
    blog_date=models.DateField(max_length=200)
    blog_comment=models.CharField(max_length=200)
    blog_author=models.CharField(max_length=50)
    blog_title=models.CharField(max_length=200)
    blog_desc=models.TextField()




# Create your models here vehicle categories.

class Vehicle(models.Model):
    vehicle_image=models.ImageField(upload_to='media/',blank=True,default='images/car-5.png')
    vehicle_title=models.CharField(max_length=200)
    vehicle_rate=models.CharField(max_length=200)
    




    # Create your models here client review.
class Review(models.Model):

    review_image=models.ImageField(upload_to='media/',blank=True,default='images/car-6.png')
    review_title=models.CharField(max_length=200)
    review_icon=models.CharField(max_length=200)
    review_desc=models.TextField()



     # Create your models here booking features.
class Booking(models.Model):

    booking_icon=models.CharField(max_length=200)
    booking_title=models.CharField(max_length=200)
    
    booking_desc=models.TextField()

# create form

class HeroForm(models.Model):
    car_type=models.CharField(max_length=100)
    pickup_location=models.CharField(max_length=100)
    drop_location=models.CharField(max_length=100)
    pickup_date=models.CharField(max_length=100)
    pickup_time=models.CharField(max_length=100)
    drop_date=models.CharField(max_length=100)
    drop_time=models.CharField(max_length=100)
    

    


    
