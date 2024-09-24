from datetime import date
from enum import Enum
from django.db import models
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser,BaseUserManager,AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager

from rdiapp.enums import Role

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

"""class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_teacher", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_teacher", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_teacher"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)"""

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

"""class CustomUser(AbstractUser):
    # Add your custom fields here
    username = models.CharField(max_length=32)
    role = models.CharField(
        max_length=10,
        choices=[(tag.name, tag.value) for tag in Role],
        default=Role.STUDENT.value
    )
    birth_date = models.DateField(null=True, blank=True)
    # You can also override existing fields
    email = models.EmailField(unique=True)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    #objects = CustomUserManager()
    pass"""

class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_abbreviation = models.CharField(max_length=30)

class SchoolClass(models.Model):
    school_class_name = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)

class SchoolClassLevel(models.Model):
    level_name = models.CharField(max_length=30)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, default=1)

class Student(CustomUser):
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

class Teacher(CustomUser):
    teacher_picture = models.ImageField(upload_to='teacher_pictures/', height_field=None, width_field=None, max_length=100)
    up = models.ForeignKey(Up, on_delete=models.CASCADE, default=1)
    research_team = models.ForeignKey(ResearchTeam, on_delete=models.CASCADE, default=1)
    is_head_supervisor = models.BooleanField(default = False)

""""
class TeamHead(models.Model):
    head_supervisor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    research_team = models.ForeignKey(ResearchTeam, on_delete=models.CASCADE, default=1)
"""

#   class Meta:
#       constraints = [
#           UniqueConstraint(fields=['head_supervisor', 'research_team'], name='unique_head_supervisor_per_team')
#       ]

class Project(models.Model):
    owners = models.ForeignKey(Teacher, related_name='rdiapp', on_delete=models.CASCADE, default=1)
    highlighted = models.TextField(default=1)
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
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

class Application(models.Model):
    owner = models.ForeignKey(Student, related_name='rdiapp', on_delete=models.CASCADE, default=1)
    highlighted = models.TextField(default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)    
