from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 null=True,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index = True)
    description = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='products_upload/', null=True) 
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
   

class ProductImage(models.Model):
    path = models.ImageField(upload_to='products_upload/')
    product = models.ForeignKey(Product,
                                 related_name='images',
                                 null=True,
                                 on_delete=models.CASCADE)
