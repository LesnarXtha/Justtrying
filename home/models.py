from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.
class Students(models.Model):
 #   id = models.AutoField() #this django automatically handles this is PK
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    Email = models.EmailField()
    address = models.TextField(null=True, blank=False)
    

class Cars(models.Model):
   car_name = models.CharField(max_length=100)
   speed = models.IntegerField(default=60)
   
   def __str__(self):
       return self.car_name

@receiver(post_save ,sender = Cars)
def call_car_api(sender,instance, **kwargs):
    print("object Created")
    print(instance)
