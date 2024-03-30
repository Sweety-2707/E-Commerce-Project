from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home.as_view()),
    path('product-detail/<int:pk>', views.product_details.as_view(), name='product_details'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('plus/', views.plus),
    path('minus/', views.minus),
    path('plus-buy-now/', views.plusbuynow),
    path('minus-buy-now/', views.minusbuynow),
    path('remove/', views.remove),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('address/', views.address.as_view(), name='address'),
    path('addaddress/', views.addaddress.as_view(), name='addaddress'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.changepassword.as_view(), name='changepassword'),
    path('men/Topwear/', views.mentopwear, name='mentopwear'),
    path('men/Topwear/<str:data>', views.mentopwear, name='mentopweardata'),
    path('men/Bottomwear/', views.menbottomwear, name='menbottomwear'),
    path('men/Bottomwear/<str:data>', views.menbottomwear, name='menbottomweardata'),
    path('women/Topwear/', views.womentopwear, name='womentopwear'),
    path('women/Topwear/<str:data>', views.womentopwear, name='womentopweardata'),
    path('women/Bottomwear/', views.womenbottomwear, name='womenbottomwear'),
    path('women/Bottomwear/<str:data>', views.womenbottomwear, name='womenbottomweardata'),
    path('login/', views.login_page.as_view(), name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('orderplaced', views.orderplaced, name='orderplaced'),
    path('cartorderplaced', views.cartorderplaced, name='cartorderplaced'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )


