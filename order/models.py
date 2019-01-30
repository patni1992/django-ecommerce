from django.db import models

class Order(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    paid = models.BooleanField(default=False)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    