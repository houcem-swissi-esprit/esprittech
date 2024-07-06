from django.db import models

# Create your models here.


class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_abbreviation = models.CharField(max_length=30)

class SchoolClass(models.Model):
    school_class_name = models.CharField(max_length=30)

class SchoolClassLevel(models.Model):
    level_name = models.CharField(max_length=30)

class Student(models.Model):
    student_name = models.CharField(max_length=32)
    student_family_name = models.CharField(max_length=32)
    student_email_address = models.EmailField(max_length=254)  # Corrected typo
    student_cv = models.FileField(upload_to='students_cvs')
    student_linkedin = models.URLField(max_length=200)
    student_picture = models.ImageField(upload_to='student_pictures/',  # Added specific directory
                                        height_field=None,
                                        width_field=None,
                                        max_length=100)
    student_graduation_year = models.PositiveIntegerField()

class UP(models.Model):
    up_name = models.CharField(max_length=32)

class Department(models.Model):
    department_name = models.CharField(max_length=32)

class ResearchDepartment(models.Model):
    research_department_name = models.CharField(max_length=32)  # Corrected typo

class ResearchTeam(models.Model):
    research_team_name = models.CharField(max_length=32)  # Corrected typo
    domain = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)  # Corrected typo for consistency
    research_team_logo = models.ImageField(upload_to='research_team_logos/',  # Added specific directory
                                           height_field=None,
                                           width_field=None,
                                           max_length=100)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=32)
    teacher_family_name = models.CharField(max_length=32)
    teacher_email_address = models.EmailField(max_length=254)  # Corrected typo
    teacher_picture = models.ImageField(upload_to='teacher_pictures/',  # Added specific directory
                                        height_field=None,
                                        width_field=None,
                                        max_length=100)

class Project(models.Model):
    title = models.TextField()
    keywords = models.TextField()
    objectives = models.TextField()  # Corrected typo
    deliverables = models.TextField()
    required_skills = models.TextField()
    details = models.FileField(upload_to='research_projects')
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    finish_date = models.DateField(auto_now=False, auto_now_add=False)
    duration_in_weeks = models.PositiveIntegerField()
    more_than_one_intern = models.BooleanField()