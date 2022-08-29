from rest_framework import serializers
from .models import Project, ProjectImplementation

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectImplementation
        fields = '__all__'