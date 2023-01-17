from .models import Instructor,Course
from rest_framework import serializers


class CourseSerializer(serializers.HyperlinkedModelSerializer): # used for hyperlinked

    class Meta:
        model = Course
        fields = '__all__'
class InstructorSerializer(serializers.HyperlinkedModelSerializer): # used for hyperlinked
    courses = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='course-detail')
    
    class Meta:
        model = Instructor
        fields = "__all__"

        