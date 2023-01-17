from django.urls import path
from .views import InstructorListView,CourseListView
urlpatterns = [
    
    path('instructors',InstructorListView.as_view(),name = 'instruct'),
    path('course',CourseListView.as_view(),name = 'courses')
]
