from django.db import models
from django.contrib.auth.models import User

# Create your models here
class category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} Category'

class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} Product'
    


class cart(models.Model):
        user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        product = models.ForeignKey(product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(self):
            return f'{self.quantity} x {self.product.name} for {self.user.username}'
class order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(default='COD', max_length=50)

    def __str__(self):
        return f'Order of {self.quantity} x {self.product.name} by {self.user.username} on {self.order_date}'
