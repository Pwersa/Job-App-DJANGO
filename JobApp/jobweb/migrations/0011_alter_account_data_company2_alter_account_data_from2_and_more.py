# Generated by Django 4.0.1 on 2022-02-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0010_alter_account_data_from1_alter_account_data_from2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_data',
            name='company2',
            field=models.CharField(default='', max_length=99, verbose_name='company2'),
        ),
        migrations.AlterField(
            model_name='account_data',
            name='from2',
            field=models.CharField(default='', max_length=99, verbose_name='from_2'),
        ),
        migrations.AlterField(
            model_name='account_data',
            name='to1',
            field=models.CharField(default='', max_length=99, verbose_name='to_1'),
        ),
        migrations.AlterField(
            model_name='account_data',
            name='to2',
            field=models.CharField(default='', max_length=99, verbose_name='to_2'),
        ),
    ]
