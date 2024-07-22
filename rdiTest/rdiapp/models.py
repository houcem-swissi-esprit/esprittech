from datetime import date
from django.db import models
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Add your custom fields here
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    # You can also override existing fields
    email = models.EmailField(unique=True)
    pass

class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_abbreviation = models.CharField(max_length=30)

class SchoolClass(models.Model):
    school_class_name = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)

class SchoolClassLevel(models.Model):
    level_name = models.CharField(max_length=30)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, default=1)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=1)
    student_cv = models.FileField(upload_to='students_cvs')
    student_linkedin = models.URLField(max_length=200)
    student_picture = models.ImageField(upload_to='student_pictures/', height_field=None, width_field=None, max_length=100)
    student_graduation_year = models.PositiveIntegerField()
    school_class_level = models.ForeignKey(SchoolClassLevel, on_delete=models.CASCADE, default=1)

class Department(models.Model):
    department_name = models.CharField(max_length=32)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)

class Up(models.Model):
    up_name = models.CharField(max_length=32)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

class ResearchDepartment(models.Model):
    research_department_name = models.CharField(max_length=32)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)


class ResearchTeam(models.Model):
    research_team_name = models.CharField(max_length=32)
    field = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    research_team_logo = models.ImageField(upload_to='research_team_logos/', height_field=None, width_field=None, max_length=100)
    research_department = models.ForeignKey(ResearchDepartment, on_delete=models.CASCADE, default=1)

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=1)
    teacher_picture = models.ImageField(upload_to='teacher_pictures/', height_field=None, width_field=None, max_length=100)
    up = models.ForeignKey(Up, on_delete=models.CASCADE, default=1)
    research_team = models.ForeignKey(ResearchTeam, on_delete=models.CASCADE, default=1)

class TeamHead(models.Model):
    head_supervisor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    research_team = models.ForeignKey(ResearchTeam, on_delete=models.CASCADE, default=1)

#   class Meta:
#       constraints = [
#           UniqueConstraint(fields=['head_supervisor', 'research_team'], name='unique_head_supervisor_per_team')
#       ]

class Project(models.Model):
    title = models.TextField()
    label = models.CharField(max_length = 32, unique = True, default= "project" )
    keywords = models.TextField()
    objectives = models.TextField()
    deliverables = models.TextField()
    required_skills = models.TextField()
    details = models.FileField(upload_to='research_projects')
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    finish_date = models.DateField(auto_now=False, auto_now_add=False)
    duration_in_weeks = models.PositiveIntegerField()
    more_than_one_intern = models.BooleanField()
    assigned = models.BooleanField(default=False)
    two_supervisors = models.BooleanField(default=False)
    supervisors = models.ManyToManyField(Teacher)
    interns = models.ManyToManyField(Student)
    date_proposed = models.DateField(default=date.today)
    date_assigned = models.DateField(default=date.today)

    def clean(self):
        if not (1 <= self.supervisors.count() <= 2):
            raise ValidationError('A project must include exactly one or two supervisors.')
        if not (1 <= self.interns.count() <= 2):
            raise ValidationError('A project must include exactly one or two interns.')

    def __str__(self):
        supervisor_names = ', '.join([supervisor.username for supervisor in self.supervisors.all()])
        return f'Project by {supervisor_names}'

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
