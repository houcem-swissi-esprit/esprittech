# Generated by Django 5.0.6 on 2024-07-20 08:28

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_department_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_abbreviation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ResearchTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_team_name', models.CharField(max_length=32)),
                ('domain', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('research_team_logo', models.ImageField(upload_to='research_team_logos/')),
                ('research_department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.researchdepartment')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=32)),
                ('school', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.school')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_class_name', models.CharField(max_length=30)),
                ('school', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.school')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClassLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=30)),
                ('school_class', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.schoolclass')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_cv', models.FileField(upload_to='students_cvs')),
                ('student_linkedin', models.URLField()),
                ('student_picture', models.ImageField(upload_to='student_pictures/')),
                ('student_graduation_year', models.PositiveIntegerField()),
                ('school_class_level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.schoolclasslevel')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('keywords', models.TextField()),
                ('objectives', models.TextField()),
                ('deliverables', models.TextField()),
                ('required_skills', models.TextField()),
                ('details', models.FileField(upload_to='research_projects')),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('duration_in_weeks', models.PositiveIntegerField()),
                ('more_than_one_intern', models.BooleanField()),
                ('assigned', models.BooleanField(default=False)),
                ('two_supervisors', models.BooleanField(default=False)),
                ('date_proposed', models.DateField(default=datetime.date.today)),
                ('date_assigned', models.DateField(default=datetime.date.today)),
                ('interns', models.ManyToManyField(to='rdiapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rdiapp.project')),
                ('student', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_picture', models.ImageField(upload_to='teacher_pictures/')),
                ('research_team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.researchteam')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='supervisors',
            field=models.ManyToManyField(to='rdiapp.teacher'),
        ),
        migrations.CreateModel(
            name='TeamHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rdiapp.teacher')),
                ('research_team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.researchteam')),
            ],
        ),
        migrations.CreateModel(
            name='Up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_name', models.CharField(max_length=32)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.department')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='up',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rdiapp.up'),
        ),
    ]
