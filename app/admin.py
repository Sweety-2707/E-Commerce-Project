from django.contrib import admin
from .models import(
    Customer,
    Product,
    cart,
    OrderPlaced,
    DealOfTheDay,
    TrendingDeals,
    Delivery_Address
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','gender','mobile','email']

@admin.register(Delivery_Address)
class DeliveryAddressModelAdmin(admin.ModelAdmin):
    list_display=['id','email','first_name','last_name','mobile','locality','city','pincode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','quantity','description','brand'
                  ,'category','sub_category','product_image']
    
@admin.register(cart)
class cartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','amount','address','order_date','status']

@admin.register(DealOfTheDay)
class DealOfTheDayModelAdmin(admin.ModelAdmin):
    list_display=['product']

@admin.register(TrendingDeals)
class TrendingDealsModelAdmin(admin.ModelAdmin):
    list_display=['product']