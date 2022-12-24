from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from students.models import Students
from students.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required, permission_required

@csrf_exempt
def studentApi(request):
    if request.method=='GET':
        token = request.COOKIES.get('jwt')
        if not token:
            return JsonResponse("Unauthenticated!",safe=False)

        students = Students.objects.all()
        students_serializer=StudentSerializer(students,many=True)        
        pagination = json.loads(request.body)['pagination']
        if pagination['first_index'] >= pagination['last_index']:
            return JsonResponse("Invalid Indexing!",safe=False)
        return JsonResponse(students_serializer.data[pagination['first_index']:pagination['last_index']],safe=False)
    elif request.method=='POST':
        token = request.COOKIES.get('jwt')
        if not token:
            return JsonResponse("Unauthenticated!",safe=False)

        student_data=JSONParser().parse(request)
        students_serializer=StudentSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        token = request.COOKIES.get('jwt')
        if not token:
            return JsonResponse("Unauthenticated!",safe=False)

        student_data=JSONParser().parse(request)
        student=Students.objects.get(email=student_data['email'])
        students_serializer=StudentSerializer(student,data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        token = request.COOKIES.get('jwt')
        if not token:
            return JsonResponse("Unauthenticated!",safe=False)
            
        student_data=JSONParser().parse(request)
        student=Students.objects.get(email=student_data['email'])
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)


