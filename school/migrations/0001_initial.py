# Generated by Django 4.2.3 on 2023-07-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('address', models.TextField(default='')),
                ('info', models.JSONField()),
            ],
            options={
                'db_table': 'school',
            },
        ),
    ]
