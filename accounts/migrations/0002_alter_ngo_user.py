# Generated by Django 4.0.6 on 2023-04-19 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='user',
            field=models.IntegerField(),
        ),
    ]
