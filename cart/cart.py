from shop.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.items = request.session.get("cart")
        
        if not self.items:
            self.items = request.session['cart'] = {}

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.items:
            self.items[product_id]+=1
        else:
           self.items[product_id] = 1

        self.save()
    
    def remove(self, product):
        if item in self.items:
            self.items[str(product.id)]-=1
            self.save()
    
    def save(self):
        self.session.modified = True
    
    def clear(self):
        del self.session['cart']
        self.save()
    
    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
    
    def __iter__(self):
        self.current = 0
        self.products = Product.objects.filter(id__in=self.items.keys())
        self.length = len(self.products)
        return self

    def __next__(self):
        if self.current < self.length:
            product = self.products[self.current]
            product.quantity = self.items[str(product.id)]
            product.total_price = product.price * product.quantity
            self.current+=1
            return product
        else:
            raise StopIteration
        
