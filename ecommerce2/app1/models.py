from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum



class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField() 
    image=models.ImageField(upload_to='image')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.CharField(max_length=50,default=0)
    color=models.CharField(max_length=20,default=0)
    size = models.DecimalField(default=0.0, max_digits=10, decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def top_selling(self):
        all_products = Product.objects.annotate(total_quantity_ordered=Sum('orderitem__quantity'))
        top_product = all_products.order_by('-total_quantity_ordered').first()
        return top_product

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(default=0)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    age=models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='OrderItem')




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # You can add additional fields if needed


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')), default=1)
    review = models.TextField()
    date=models.DateTimeField(auto_now_add=True)
 
class ProductImages(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    image1 =models.ImageField(upload_to="image1",default=0)
    image2 =models.ImageField(upload_to="image2",default=0)
    image3 =models.ImageField(upload_to="image3",default=0)

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='WishListItem')




class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ShippingAddress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='shipping_addresses')
    name = models.CharField(max_length=100)  # Name of the recipient
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100,null=True)
    zip_code = models.CharField(max_length=20)
    

    def __str__(self):
        return f"{self.name} - {self.address}, {self.city}, {self.city}, {self.zip_code}"
    
class OrderPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100,blank =True)
    amount=models.IntegerField(default=0)
    paid=models.BooleanField(default=False)
    products = models.JSONField(default=dict)

    def __str__(self):
        return self.order_id