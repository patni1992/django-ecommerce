# Generated by Django 2.1.5 on 2019-02-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
