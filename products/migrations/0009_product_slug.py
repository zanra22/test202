# Generated by Django 4.0.3 on 2022-09-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_active_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='tae'),
        ),
    ]
