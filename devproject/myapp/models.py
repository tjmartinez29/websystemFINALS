from django.db import models
 
# Create your models here.
class Employee(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    address = models.CharField(max_length=500) 
    image = models.ImageField(upload_to='images/', null=True, blank=True)
   
    class Meta:  
        db_table = "tblemployee"