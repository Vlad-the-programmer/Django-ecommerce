# Generated by Django 4.2.1 on 2023-11-05 13:28

import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_category_image_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category.jpg', upload_to='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product.jpg', upload_to=product.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='cover_image',
            field=models.ImageField(default='vendor-cover.jpg', upload_to=product.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(default='vendor.jpg', upload_to=product.models.user_directory_path),
        ),
    ]
