# Generated by Django 4.0.6 on 2023-04-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_ngo_true'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
