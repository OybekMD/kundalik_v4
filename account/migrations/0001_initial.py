# Generated by Django 4.2.3 on 2023-07-14 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('username', models.CharField(default='', max_length=25)),
                ('password', models.CharField(default='', max_length=65)),
                ('phone', models.CharField(default='', max_length=65)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('toifa', models.CharField(default='', max_length=65)),
                ('salary', models.PositiveIntegerField(default=1)),
                ('school', models.ManyToManyField(to='school.schoolmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
