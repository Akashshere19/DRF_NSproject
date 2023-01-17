from django.contrib import admin
from .models import Instructor,Course
# Register your models here.
class AdminInstructor(admin.ModelAdmin):
    list_display = ['name','email']

class AdminCourse(admin.ModelAdmin):
    list_display = ['title','rating']

admin.site.register(Instructor,AdminInstructor)    
admin.site.register(Course,AdminCourse) 