# Generated by Django 3.1.2 on 2020-10-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20201006_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Unique_Squirrel_ID',
            field=models.CharField(max_length=100),
        ),
    ]
