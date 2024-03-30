from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

state_choices=(
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunanchal Pradesh','Arunanchal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhatisgarh','Chhatisgarh'),
    ('Dadar & Nagar Haveli','Dadar & Nagar Haveli'),
    ('Daman & Diu','Daman & Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Ladhak','Ladhak'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
)
gender_choices=(
    ('Male','Male'),
    ('Female','Female'),
)

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    gender=models.CharField(choices=gender_choices,max_length=10,blank=True, null=True)
    mobile=models.IntegerField(blank=True, null=True)
    email=models.EmailField(max_length=200)

    def __str__(self):
        return str(self.id)

class Delivery_Address(models.Model):
    email=models.EmailField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    mobile=models.IntegerField(blank=True, null=True)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField(blank=True, null=True)
    state=models.CharField(choices=state_choices,max_length=50)

    def __str__(self):
        return str(self.id)
    
category_choices=(
    ('Men','Men'),
    ('Women','Women'),
)
sub_category_choices=(
    ('Top Wear','Top Wear'),
    ('Bottom Wear','Bottom Wear'),
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    quantity=models.IntegerField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=category_choices,max_length=20)
    sub_category=models.CharField(choices=sub_category_choices,max_length=50)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
status_choices=(
    ('Order Placed','Order Placed'),
    ('Accepted','Accepted'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
    ('Cancelled','Cancelled'),
    ('Return Request','Return Request'),
    ('Returned','Returned'),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    amount=models.FloatField()
    address=models.ForeignKey(Delivery_Address,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=status_choices ,max_length=50, default='Pending')

    def __str__(self):
        return str(self.id)
    
class DealOfTheDay(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class TrendingDeals(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
