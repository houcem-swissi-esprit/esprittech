from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics , permissions
from rdiapp.permissions import IsOwnerOrReadOnly
from rdiapp.models import *
from rdiapp.enums import *
from rest_framework.decorators import api_view
from rdiapp.serializers import generated_serializers

# Create your views here.

"""
def index(request):
    return HttpResponse("You're looking to the index page.")
"""

def index(request):
    return render(request, 'rdiapp/Templates/index.html') 

class ProjectList(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = generated_serializers["ProjectSerializer"]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    

class ProjectCreate(generics.CreateAPIView):  
    queryset = Project.objects.all()
    serializer_class = generated_serializers["ProjectSerializer"]

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = generated_serializers["ProjectSerializer"]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class ResearchTeamDetail(generics.RetrieveAPIView):
    queryset = ResearchTeam.objects.all()
    serializer_class = generated_serializers["ResearchTeamSerializer"]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = generated_serializers["ApplicationSerializer"]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    

class ApplicationCreate(generics.CreateAPIView):  
    queryset = Application.objects.all()
    serializer_class = generated_serializers["ApplicationSerializer"]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = generated_serializers["TeacherSerializer"]   

class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = generated_serializers["StudentSerializer"]      



    
    

    
