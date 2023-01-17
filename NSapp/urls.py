from django.urls import path
from .views import InstructorListView,CourseListView,CourseDetailView,InstructorDetailView
urlpatterns = [
    
    path('instructors',InstructorListView.as_view(),name = 'instruct'),
    path('course',CourseListView.as_view(),name = 'courses'),
    path('course/<int:pk>',CourseDetailView.as_view(),name = 'course-detail'),# used for hyperlinked
    path('instructors/<int:pk>',InstructorDetailView.as_view(),name = 'instructor-detail'),# used for hyperlinked
]
