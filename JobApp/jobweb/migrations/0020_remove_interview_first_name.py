# Generated by Django 4.0.1 on 2022-05-05 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0019_remove_interview_name_interview_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='first_name',
        ),
    ]
