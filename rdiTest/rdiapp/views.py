from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rdiapp.models import Application, Project, ResearchTeam
from rdiapp.serializers import generated_serializers

# Create your views here.

def index(request):
    return HttpResponse("You're looking to the index page.")

class ProjectList(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = generated_serializers["ProjectSerializer"]

class ProjectCreate(generics.CreateAPIView):  
    queryset = Project.objects.all()
    serializer_class = generated_serializers["ProjectSerializer"]

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = generated_serializers["ProjectSerializer"]

class ResearchTeamDetail(generics.RetrieveAPIView):
    queryset = ResearchTeam.objects.all()
    serializer_class = generated_serializers["ResearchTeamSerializer"]


class ApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = generated_serializers["ApplicationSerializer"]

class ApplicationCreate(generics.CreateAPIView):  
    queryset = Application.objects.all()
    serializer_class = generated_serializers["ProjectSerializer"]

    
