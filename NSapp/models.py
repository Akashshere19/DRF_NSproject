from django.db import models


# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    
    def __str__(self):
        return self.email  

class Course(models.Model):
    title  = models.CharField(max_length=30)
    rating = models.EmailField()
    instructor  = models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name='courses')          