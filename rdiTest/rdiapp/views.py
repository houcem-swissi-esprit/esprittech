from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import generics , permissions , viewsets
from rdiapp.permissions import IsOwnerOrReadOnly
from rdiapp.models import *
from rdiapp.enums import *
from rest_framework.decorators import api_view
from rdiapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


def index(request):
    return HttpResponse("You're looking to the index page.")

"""

def index(request):
    return render(request, 'index.html') 
"""



"""class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

"""
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserRegisterSerializer(user, context=self.get_serializer_context()).data,
            "message": "User registered successfully",
        }, status=status.HTTP_201_CREATED)
        """

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

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

class RoleChoiceView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RoleChoiceSerializer(data=request.data)
        if serializer.is_valid():
            role = serializer.validated_data['role']
            if role == Role.TEACHER.value:
                return redirect('teacher-create')
            elif role == Role.STUDENT.value:
                return redirect('student-create')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = generated_serializers["TeacherSerializer"]  
"""

class TeacherCreate(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = generated_serializers["TeacherSerializer"]   

class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = generated_serializers["StudentSerializer"]     



    
    

    
