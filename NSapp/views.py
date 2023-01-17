from django.shortcuts import render
from .models import Course,Instructor
from rest_framework import generics
from .serializers import InstructorSerializer,CourseSerializer
# Create your views here.
class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

# used for Hyper linked
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()    

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()    