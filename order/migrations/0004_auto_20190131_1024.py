# Generated by Django 2.1.5 on 2019-01-31 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cities_light.City'),
        ),
    ]
