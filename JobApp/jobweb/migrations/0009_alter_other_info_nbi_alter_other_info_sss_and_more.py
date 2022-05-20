# Generated by Django 4.0.4 on 2022-05-20 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0008_alter_other_info_nbi_alter_other_info_sss_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_info',
            name='NBI',
            field=models.CharField(blank=True, default='', max_length=99, null=True, verbose_name='NBI'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='SSS',
            field=models.CharField(blank=True, default='', max_length=99, null=True, verbose_name='SSS'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='TIN',
            field=models.CharField(blank=True, default='', max_length=99, null=True, verbose_name='TIN'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='med_record',
            field=models.CharField(blank=True, default='', max_length=6, null=True, verbose_name='med_record'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='pagibig',
            field=models.CharField(blank=True, default='', max_length=99, null=True, verbose_name='pagibig'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='philhealth',
            field=models.CharField(blank=True, default='', max_length=99, null=True, verbose_name='philhealth'),
        ),
    ]
