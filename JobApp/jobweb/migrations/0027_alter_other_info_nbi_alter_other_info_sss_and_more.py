# Generated by Django 4.0.1 on 2022-05-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0026_alter_other_info_position2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_info',
            name='NBI',
            field=models.CharField(max_length=99, null=True, verbose_name='NBI'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='SSS',
            field=models.CharField(max_length=99, null=True, verbose_name='SSS'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='TIN',
            field=models.CharField(max_length=99, null=True, verbose_name='TIN'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='college_grad',
            field=models.CharField(max_length=99, null=True, verbose_name='college_grad'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='e_no',
            field=models.CharField(max_length=99, null=True, verbose_name='e_no'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='elementary_grad',
            field=models.CharField(max_length=99, null=True, verbose_name='elementary_grad'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='highschool_grad',
            field=models.CharField(max_length=99, null=True, verbose_name='highschool_grad'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='pagibig',
            field=models.CharField(max_length=99, null=True, verbose_name='pagibig'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='philhealth',
            field=models.CharField(max_length=99, null=True, verbose_name='philhealth'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='refcon1',
            field=models.CharField(default='', max_length=99, null=True, verbose_name='refcon1'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='refcon2',
            field=models.CharField(default='', max_length=99, null=True, verbose_name='refcon2'),
        ),
    ]