# Generated by Django 2.1.5 on 2019-01-18 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190118_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='mainImage',
            new_name='main_Image',
        ),
    ]
