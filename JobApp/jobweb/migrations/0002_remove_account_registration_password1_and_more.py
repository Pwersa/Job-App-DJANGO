# Generated by Django 4.0.1 on 2022-05-18 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_registration',
            name='password1',
        ),
        migrations.AddField(
            model_name='account_registration',
            name='password2',
            field=models.CharField(default='', max_length=20, verbose_name='password2'),
        ),
    ]