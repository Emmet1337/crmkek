# Generated by Django 3.0 on 2019-12-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20191217_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealscategory',
            old_name='department',
            new_name='departmentid',
        ),
        migrations.AlterField(
            model_name='mealscategory',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
