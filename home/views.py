from django.shortcuts import render,redirect
from .models import Product,Customer,Order,OrededItem
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

# Create your views here.

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        else:

            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
            customer=Customer.objects.create(
                username=uname,
                user=my_user,
                phone=phone,
                address=address
            )
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or Password is incorrect!!!")
            return redirect('login')

    return render (request,'login.html')

def pdt_detail(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}

    return render(request,'product_details.html',context)

def loggout(request):
    logout(request)
    return redirect('login')

def home(request):
    feature_list = Product.objects.order_by('priority')[:4]
    latest_list = Product.objects.order_by('-id')[:4]
    dict_home={
        'f_list':feature_list,
        'l_list':latest_list
    }
    return render(request,'index.html',dict_home)

def products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    list = Product.objects.order_by('priority')
    p = Paginator(list,4)
    list = p.get_page(page)
    dict = {'product':list}
    return render(request,'products.html',dict)

def account(request):
    return render(request,'account.html')


def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(pk=product_id)
        ordered_item,created=OrededItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if created:
            ordered_item.quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()

        return redirect('cart')

def cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def remove_item_cart(request,pk):
    item=OrededItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.save()
                status_message="your order is confirmed"
                messages.success(request,status_message)
            else:
                status_message="No item found"
                messages.error(request,status_message)
        except Exception as error:
            status_message="No item found"
            messages.error(request,status_message)
    return redirect('checkoutpage')