# Generated by Django 4.0.1 on 2022-05-05 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0023_alter_other_info_nbi_alter_other_info_sss_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_registration',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='first_name',
        ),
    ]