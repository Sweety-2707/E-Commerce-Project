from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from .models import Customer,Product,cart,OrderPlaced,DealOfTheDay,TrendingDeals,Delivery_Address
from .forms import CustomerRegistrationForm, LoginForm,ChangePassword,AddressForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse

class home(View):
 def get(self,request):
  cartitem=0
  if request.user.is_authenticated:
    cartitem=len(cart.objects.filter(user=request.user))
  Dealofthedayproduct=DealOfTheDay.objects.all()
  TrendingDeal=TrendingDeals.objects.all()
  return render(request,'app/home.html',{'Dealofthedayproduct':Dealofthedayproduct
                                         ,'TrendingDeal':TrendingDeal,"cartitem":cartitem})
 
class product_details(View):
 def get(self,request,pk):
  cartitem=0
  if request.user.is_authenticated:
       cartitem=len(cart.objects.filter(user=request.user))
  product=Product.objects.get(pk=pk)
  return render(request,'app/productdetail.html',{'product':product,"cartitem":cartitem})
  

def add_to_cart(request):
 cartitem=0
 if request.user.is_authenticated:
    cartitem=len(cart.objects.filter(user=request.user))
    user=request.user
    prod_id=request.GET.get("product_id")
    product=Product.objects.get(id=prod_id)
    if cart.objects.filter(user=user,product=product).exists():
      messages.warning(request,"Product already Present in Cart")
      return redirect("/cart/")
    else:
      if product.quantity>0:
        cart(user=user,product=product).save()
        return redirect("/cart/")
      else:
        messages.warning(request,"Product is Out of Stock")
        return redirect('product_details',prod_id)
 else:
   return redirect("/login/")

def buy_now(request):
 if request.user.is_authenticated:
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    user=request.user
    prod_id=request.GET.get("product_id")
    product=Product.objects.get(id=prod_id)
    add=Delivery_Address.objects.filter(email=request.user.email)
    amount=Product.objects.get(id=prod_id).discounted_price
    totalamount=0.0
    if amount>=500:
      shipping_amount=0.0
    else:
      shipping_amount=50.0
    if product.quantity>0:
      totalamount = amount+shipping_amount
      return render(request, 'app/buynow.html',{"product":product,"add":add,"totalamount":totalamount,"amount":amount,"shipping_amount":shipping_amount,"cartitem":cartitem})
    else:
      messages.warning(request,"Product is Out of Stock")
      return redirect('product_details',prod_id)
 else:
   return redirect("/login/")

def plusbuynow(request):
  if request.method=="GET":
      prod_id=request.GET['prod_id']
      user=request.user
      quantity=int(request.GET['quantity'])
      product=Product.objects.get(id=prod_id)
      pamt=product.discounted_price
      if product.quantity>quantity:
        quantity+=1
      amount=quantity*pamt
      totalamount=0.0
      if amount>=500:
        shipping_amount=0.0
      else:
        shipping_amount=50.0
           
      totalamount = amount+shipping_amount
      data={
          'quantity':quantity,
          'shipping_amount':shipping_amount,
          'amount':amount,
          'totalamount':totalamount
        }
      return JsonResponse(data)
       

  
def minusbuynow(request):
  if request.method=="GET":
      prod_id=request.GET['prod_id']
      user=request.user
      quantity=int(request.GET['quantity'])
      product=Product.objects.get(id=prod_id)
      pamt=product.discounted_price
      if quantity>1:
        quantity-=1
      
      amount=quantity*pamt
      totalamount=0.0
      if amount>=500:
        shipping_amount=0.0
      else:
        shipping_amount=50.0
      totalamount = amount+shipping_amount
      data={
          'quantity':quantity,
          'shipping_amount':shipping_amount,
          'amount':amount,
          'totalamount':totalamount
        }
      return JsonResponse(data)

def orderplaced(request):
  if request.user.is_authenticated:
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    user=request.user  
    customer=Customer.objects.filter(email=request.user.email).get()
    prod_id=request.POST.get("product_id")
    product=Product.objects.get(id=prod_id)
    quantity=request.POST.get("quan")
    add=request.POST.get("delivery_add_id")
    address=Delivery_Address.objects.get(id=add)
    totalamount=request.POST.get("tamount")
    OrderPlaced(user=user,customer=customer,product=product,quantity=quantity,amount=totalamount,address=address).save()
    product.quantity-=int(quantity)
    product.save()
    return render(request,"app/orderplaced.html",{"cartitem":cartitem})
  


def show_cart(request):
  if request.user.is_authenticated:
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    user=request.user
    Cart=cart.objects.filter(user=user)
    amount=0.0
    totalamount=0.0
    if Cart:
      for c in Cart:
        tempamount=(c.quantity * c.product.discounted_price)
        amount +=tempamount
        if amount>=500:
          shipping_amount=0.0
        else:
          shipping_amount=50.0
        totalamount = amount+shipping_amount
      return render(request, 'app/addtocart.html',{"Cart":Cart,"totalamount":totalamount,"amount":amount,"shipping_amount":shipping_amount,"cartitem":cartitem})
    else:
      return render(request,'app/emptycart.html')
  
def plus(request):
  if request.method=="GET":
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    prod_id=request.GET['prod_id']
    product=Product.objects.get(id=prod_id)
    Cart=cart.objects.get(user=request.user,product=prod_id)
    if product.quantity>Cart.quantity:
      Cart.quantity+=1
    Cart.save()
    C=Cart.quantity
    user=request.user
    Cart=cart.objects.filter(user=user)
    amount=0.0
    totalamount=0.0
    if Cart:
      for c in Cart:
        tempamount=(c.quantity * c.product.discounted_price)
        amount +=tempamount
        if amount>=500:
          shipping_amount=0.0
        else:
          shipping_amount=50.0
        totalamount = amount+shipping_amount
        
      data={
        'quantity':C,
        'shipping_amount':shipping_amount,
        'amount':amount,
        'totalamount':totalamount
      }
      
      return JsonResponse(data)
    else:
      return render(request,'app/emptycart.html',{"cartitem":cartitem})
  
def minus(request):
  if request.method=="GET":
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    prod_id=request.GET['prod_id']
    product=Product.objects.get(id=prod_id)
    Cart=cart.objects.get(user=request.user,product=prod_id)
    if Cart.quantity>1:
      Cart.quantity-=1
    Cart.save()
    C=Cart.quantity
    user=request.user
    Cart=cart.objects.filter(user=user)
    amount=0.0
    totalamount=0.0
    if Cart:
      for c in Cart:
        tempamount=(c.quantity * c.product.discounted_price)
        amount +=tempamount
        if amount>=500:
          shipping_amount=0.0
        else:
          shipping_amount=50.0
        totalamount = amount+shipping_amount
        
      data={
        'quantity':C,
        'shipping_amount':shipping_amount,
        'amount':amount,
        'totalamount':totalamount
      }
      
      return JsonResponse(data)
    else:
      return render(request,'app/emptycart.html',{"cartitem":cartitem})
  
def remove(request):
  if request.method=="GET":
      cartitem=0
      cartitem=len(cart.objects.filter(user=request.user))
      prod_id=request.GET['prod_id']
      c=cart.objects.get(user=request.user,product=prod_id)
      c.delete()
      user=request.user
      Cart=cart.objects.filter(user=user)
      amount=0.0
      totalamount=0.0
      if Cart:
        for c in Cart:
          tempamount=(c.quantity * c.product.discounted_price)
          amount +=tempamount
          if amount>=500:
            shipping_amount=0.0
          else:
            shipping_amount=50.0
          totalamount = amount+shipping_amount
        data={
          'shipping_amount':shipping_amount,
          'amount':amount,
          'totalamount':totalamount
        }
        return JsonResponse(data)
      else:
         return render(request,'app/emptycart.html',{"cartitem":cartitem})
  
class profile(View):
  def get(self,request):
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    customer=Customer.objects.filter(email=request.user.email)
    return render(request, "app/profile.html", {"customer": customer,"cartitem":cartitem})
 
  def post(self,request):
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    customer=Customer.objects.filter(email=request.user.email)
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    gender=request.POST.get('gender')
    mobile=request.POST.get('mobile')
    email=request.POST.get('email')
    if email!=request.user.email:
      if User.objects.filter(email=email):
        messages.warning(request,"Email Already Exists!")
        return render(request, "app/profile.html", {"customer": customer,"cartitem":cartitem})
      else:
       c=Customer.objects.filter(email=request.user.email).get()
       u=User.objects.filter(email=request.user.email).get()
       c.first_name=fname
       u.first_name=fname
       c.last_name=lname
       u.last_name=lname
       c.gender=gender
       c.mobile=mobile
       c.email=email
       u.email=email
       c.save()
       u.save()
       messages.success(request,"You have Successfully Updated your Profile!")
       return render(request, "app/profile.html", {"customer": customer,"cartitem":cartitem})
        
    else:
     c=Customer.objects.filter(email=request.user.email).get()
     u=User.objects.filter(email=request.user.email).get()
     c.first_name=fname
     u.first_name=fname
     c.last_name=lname
     u.last_name=lname
     c.gender=gender
     c.mobile=mobile
     c.email=email
     u.email=email
     c.save()
     u.save()
     messages.success(request,"You have Successfully Updated your Profile!")
     return render(request, "app/profile.html", {"customer": customer,"cartitem":cartitem})


class address(View):
  def get(self,request):
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    add=Delivery_Address.objects.filter(email=request.user.email)
    return render(request, "app/address.html",{"add":add,"cartitem":cartitem})
 
  
class addaddress(View):
  def get(self,request):
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    form=AddressForm()
    return render(request, "app/addaddress.html", {"form": form,"cartitem":cartitem})
 
  def post(self,request):
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    form=AddressForm(request.POST)
    if form.is_valid():
      user=Delivery_Address(email=request.user.email,first_name=form["first_name"].value(),
                          last_name=form["last_name"].value(),
                          mobile=form["mobile"].value(),
                          locality=form["locality"].value(),
                          city=form["city"].value(),
                          state=form["state"].value(),
                          pincode=form["pincode"].value(),)
      user.save()
      messages.success(request,"You have Successfully Added Address!")
      return redirect("address")
    else:
     return render(request, "app/addaddress.html", {"form": form,"cartitem":cartitem})

def orders(request):
  cartitem=0
  cartitem=len(cart.objects.filter(user=request.user))
  order=OrderPlaced.objects.filter(user=request.user)
  return render(request, 'app/orders.html',{"order":order,"cartitem":cartitem})

def mentopwear(request,data=None):
 cartitem=0
 if request.user.is_authenticated:
    cartitem=len(cart.objects.filter(user=request.user))
 if data == None:
  products=Product.objects.filter(category="Men").filter(sub_category="Top Wear")
 elif data == "Levis" or data == 'Tokyo Talkies' or data == "Roadster" or data == "Fab Star":
  products=Product.objects.filter(category="Men").filter(sub_category="Top Wear").filter(brand=data)
 elif data == "below":
  products=Product.objects.filter(category="Men").filter(sub_category="Top Wear").filter(discounted_price__lt=500)
 elif data == "above":
  products=Product.objects.filter(category="Men").filter(sub_category="Top Wear").filter(discounted_price__gt=500)
 return render(request, 'app/mentopwear.html',{'products':products,"cartitem":cartitem})

def menbottomwear(request,data=None):
 cartitem=0
 if request.user.is_authenticated:
    cartitem=len(cart.objects.filter(user=request.user))
 if data == None:
  products=Product.objects.filter(category="Men").filter(sub_category="Bottom Wear")
 elif data == "Levis" or data == 'Tokyo Talkies' or data == "Roadster" or data == "Fab Star":
  products=Product.objects.filter(category="Men").filter(sub_category="Bottom Wear").filter(brand=data)
 elif data == "below":
  products=Product.objects.filter(category="Men").filter(sub_category="Bottom Wear").filter(discounted_price__lt=500)
 elif data == "above":
  products=Product.objects.filter(category="Men").filter(sub_category="Bottom Wear").filter(discounted_price__gt=500)
 return render(request, 'app/menbottomwear.html',{'products':products,"cartitem":cartitem})

def womentopwear(request,data=None):
 cartitem=0
 if request.user.is_authenticated:
    cartitem=len(cart.objects.filter(user=request.user))
 if data == None:
  products=Product.objects.filter(category="Women").filter(sub_category="Top Wear")
 elif data == "Levis" or data == 'Tokyo Talkies' or data == "Roadster" or data == "Fab Star":
  products=Product.objects.filter(category="Women").filter(sub_category="Top Wear").filter(brand=data)
 elif data == "below":
  products=Product.objects.filter(category="Women").filter(sub_category="Top Wear").filter(discounted_price__lt=500)
 elif data == "above":
  products=Product.objects.filter(category="Women").filter(sub_category="Top Wear").filter(discounted_price__gt=500)
 return render(request, 'app/womentopwear.html',{'products':products,"cartitem":cartitem})

def womenbottomwear(request,data=None):
 cartitem=0
 if request.user.is_authenticated:
    cartitem=len(cart.objects.filter(user=request.user))
 if data == None:
  products=Product.objects.filter(category="Women").filter(sub_category="Bottom Wear")
 elif data == "Levis" or data == 'Tokyo Talkies' or data == "Roadster" or data == "Fab Star":
  products=Product.objects.filter(category="Women").filter(sub_category="Bottom Wear").filter(brand=data)
 elif data == "below":
  products=Product.objects.filter(category="Women").filter(sub_category="Bottom Wear").filter(discounted_price__lt=500)
 elif data == "above":
  products=Product.objects.filter(category="Women").filter(sub_category="Bottom Wear").filter(discounted_price__gt=500)
 return render(request, 'app/womenbottomwear.html',{'products':products,"cartitem":cartitem})

class login_page(View):
  def get(self,request):
    form=LoginForm()
    return render(request, "app/login.html", {"form": form})
 
  def post(self,request):
    form=LoginForm(request.POST)
    username=form["username"].value()
    password=form["password"].value()
    if username!="":
      if not User.objects.filter(username=username).exists():
        messages.warning(request,"You are not Registere!")
        return render(request, 'app/login.html',{"form":form})
   
      user=authenticate(username=username,password=password)
      if user is None:
       messages.warning(request,"You Password is Incorrect!")
       return render(request, 'app/login.html',{"form":form})
      else:
       login(request,user)
       return redirect("/")
    else:
      return render(request, 'app/login.html',{"form":form})
   

class customerregistration(View):
  def get(self,request):
    form=CustomerRegistrationForm()
    return render(request, "app/customerregistration.html", {"form": form})
 
  def post(self,request):
    form=CustomerRegistrationForm(request.POST)
    first_name=form["first_name"].value()
    last_name=form["last_name"].value()
    username=form["username"].value()
    email=form["email"].value()
    password=form["password"].value()
    cpassword=form["cpassword"].value()

    if password!=cpassword:
     messages.warning(request,"Password and Confirm Password Must be Same")
     return render(request, "app/customerregistration.html", {"form": form})
    
    elif User.objects.filter(email=email):
     messages.warning(request,"Email Already Exists!")
     return render(request, "app/customerregistration.html", {"form": form})
    else:
      if form.is_valid():
        user=User.objects.create(
           email=email,
           username=username,
           first_name=first_name,
           last_name=last_name
        )
        user.set_password(password)
        messages.success(request,"Congratualtions!! You have Successfully Registered")
        form.save()
        user.save()
        return render(request, "app/customerregistration.html", {"form": form})

    return render(request, "app/customerregistration.html",{"form": form})



def logout_page(request):
 logout(request)
 return redirect("/")

class changepassword(View):
  def get(self,request):
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    form=ChangePassword()
    return render(request, "app/changepassword.html", {"form": form,"cartitem":cartitem})
 
  def post(self,request):
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    form=ChangePassword(request.POST)
    password=form["password"].value()
    new_password=form["new_password"].value()
    new_password2=form["new_password2"].value()

    if new_password!=new_password2:
     messages.warning(request,"Password and Confirm Password Must be Same")
     return render(request, "app/changepassword.html", {"form": form})
    else:
      if form.is_valid():
        user=authenticate(username=request.user.username,password=password)
        if user is None:
           messages.warning(request,"Old Password is Incorrect!")
           return render(request, "app/changepassword.html", {"form": form})
        else:
           user.set_password(new_password)
           user.save()
           messages.success(request,"Password Changed Successfully!")
           return render(request, "app/changepassword.html", {"form": form})
      return render(request, "app/changepassword.html", {"form": form,"cartitem":cartitem})
    
def checkout(request):
 if request.user.is_authenticated:
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    user=request.user
    Cart=cart.objects.filter(user=user)
    add=Delivery_Address.objects.filter(email=request.user.email)
    amount=0.0
    totalamount=0.0
    for c in Cart:
      tempamount=(c.quantity * c.product.discounted_price)
      amount +=tempamount
      if amount>=500:
        shipping_amount=0.0
      else:
        shipping_amount=50.0
      totalamount = amount+shipping_amount
    return render(request, 'app/checkout.html',{"Cart":Cart,"add":add,"totalamount":totalamount,"amount":amount,"shipping_amount":shipping_amount,"cartitem":cartitem})
 
def cartorderplaced(request):
  if request.user.is_authenticated:
    cartitem=0
    cartitem=len(cart.objects.filter(user=request.user))
    user=request.user  
    customer=Customer.objects.filter(email=request.user.email).get()
    Cart=cart.objects.filter(user=user)
    for c in Cart:
      user=request.user  
      customer=Customer.objects.filter(email=request.user.email).get()
      prod_id=c.product.id
      product=Product.objects.get(id=prod_id)
      quantity=c.quantity
      add=request.POST.get("delivery_add_id")
      shipping_amount=request.POST.get("sa")
      shipping_amount=float(float(shipping_amount)/len(Cart))
      totalamount=shipping_amount+(c.quantity * c.product.discounted_price)
      address=Delivery_Address.objects.get(id=add)
      OrderPlaced(user=user,customer=customer,product=product,quantity=quantity,amount=totalamount,address=address).save()
      product.quantity-=int(quantity)
      product.save()
      c.delete()
    return render(request,"app/orderplaced.html",{"cartitem":cartitem})

