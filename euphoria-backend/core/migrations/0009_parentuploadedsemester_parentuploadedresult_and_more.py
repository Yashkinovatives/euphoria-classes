# Generated by Django 5.1.6 on 2025-03-15 16:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentUploadedSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Annual', 'Annual')], max_length=20)),
                ('year', models.IntegerField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('uploaded_by', models.ForeignKey(limit_choices_to={'user_type': 'parent'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParentUploadedResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to='parent_uploaded_results/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parentuploadedsemester')),
            ],
        ),
        migrations.CreateModel(
            name='ParentUploadedSubjectResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('marks_obtained', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_results', to='core.parentuploadedsemester')),
            ],
        ),
    ]
