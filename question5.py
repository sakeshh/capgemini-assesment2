# 5. Create a `Product` class with attributes `name`, `price`, and `stock`.
#  Write a method `check_availability(quantity)` that returns whether 
# the requested quantity is available.

class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if self.stock>=quantity:
            return "available"
        else:
            return "not available"

product=Product("chicken",200,2000)
print(product.check_availability(3000))
