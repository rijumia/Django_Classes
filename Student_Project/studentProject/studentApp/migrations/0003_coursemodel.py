# Generated by Django 5.2.1 on 2025-05-31 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0002_teachermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=100)),
                ('Course_Code', models.IntegerField(max_length=9)),
                ('Course_Instructor', models.CharField()),
                ('Course_Credits', models.IntegerField(max_length=9)),
                ('Course_Description', models.TextField(max_length=200)),
            ],
        ),
    ]
