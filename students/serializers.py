from rest_framework import serializers
from students.models import Students
from rest_framework.permissions import IsAuthenticated


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Students 
        fields=('name','email','address','city','grade','section')