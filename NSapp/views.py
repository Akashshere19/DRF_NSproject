from django.shortcuts import render
from .models import Course,Instructor
from rest_framework import generics
from .serializers import InstructorSerializer,CourseSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class WriteAdminOnlyPermisions(BasePermission):
     def has_permission(self,request,view):
        user = request.user
        if request.method == 'GET':
          return True
        if request.method == 'POST' or request.method == 'PUT' or  request.method == 'DELETE':
            if user.is_superuser:
                return True   
        return False

class InstructorListView(generics.ListCreateAPIView):
    authentications_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class CourseListView(generics.ListCreateAPIView):
    authentications_classes = [IsAuthenticated,BasicAuthentication]
    permission_classes = [WriteAdminOnlyPermisions]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

# used for Hyper linked
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()    

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()    