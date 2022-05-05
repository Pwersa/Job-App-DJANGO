# Generated by Django 4.0.1 on 2022-05-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0018_remove_interview_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='name',
        ),
        migrations.AddField(
            model_name='interview',
            name='first_name',
            field=models.CharField(default='', max_length=99, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='interview',
            name='last_name',
            field=models.CharField(default='', max_length=99, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='interview',
            name='middle_name',
            field=models.CharField(default='', max_length=99, null=True, verbose_name='middle_name'),
        ),
    ]
