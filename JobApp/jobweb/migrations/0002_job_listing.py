# Generated by Django 4.0.1 on 2022-01-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_listing',
            fields=[
                ('jtitle', models.CharField(max_length=99, primary_key=True, serialize=False, verbose_name='job_title')),
                ('jdesc', models.TextField(max_length=300, verbose_name='job_description')),
                ('no_dipl', models.BooleanField()),
                ('hs_grad', models.BooleanField()),
                ('col_grad', models.BooleanField()),
                ('no_char', models.BooleanField()),
                ('char_ref1', models.BooleanField()),
                ('char_ref2', models.BooleanField()),
                ('salary', models.PositiveIntegerField(max_length=7, verbose_name='salary')),
            ],
        ),
    ]