# Generated by Django 4.0.4 on 2022-05-23 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0014_alter_other_info_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_info',
            name='signature',
            field=models.ImageField(null=True, upload_to='signature/', verbose_name='signature'),
        ),
    ]
