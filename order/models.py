from django.db import models
from shop.models import Product
from cities_light.models import Country, City

class Order(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    paid = models.BooleanField(default=False)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Order {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def create_mail(self, cart):
        mail = {}
        cartItems = ''

        for item in cart:
                cartItems += f"product: {item} quantity: {item.quantity}\n"

        mail['from_email'] = 'admin@myshop.com'
        mail['recipient_list'] = [self.email]
        mail['subject'] =  f"Order nr. {self.id}"
        mail['message'] = f"Dear {self.first_name},\n\nYou have successfully placed an order.\nYour order id is {self.id}. \n\n{cartItems}"

        return mail

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
            return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quantity
        
    