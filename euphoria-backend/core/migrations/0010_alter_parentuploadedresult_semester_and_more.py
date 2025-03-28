# Generated by Django 5.1.6 on 2025-03-16 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_parentuploadedsemester_parentuploadedresult_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentuploadedresult',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_documents', to='core.parentuploadedsemester'),
        ),
        migrations.AlterField(
            model_name='parentuploadedsemester',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_semesters', to='core.student'),
        ),
        migrations.AlterField(
            model_name='parentuploadedsemester',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='parentuploadedsubjectresult',
            name='marks_obtained',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='parentuploadedsubjectresult',
            name='total_marks',
            field=models.PositiveIntegerField(),
        ),
    ]
