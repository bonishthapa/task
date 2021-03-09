from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Employee(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='employee')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='employee_pic',null=True,blank=True)      

    class Meta:
        ordering =('id','name')

    def __str__(self):
        return self.name

