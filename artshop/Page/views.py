from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime


def top(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        cartItems = order['get_cart_item']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'Page/first.html', context)


def pencil_art(request):
    return render(request, 'Page/pencil art.html')


def watercolor(request):
    return render(request, 'Page/watercolor.html')


def digital_art(request):
    return render(request, 'Page/digital art.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        cartItems = order['get_cart_item']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'Page/cart.html', context)


def like(request):
    return render(request, 'Page/like.html')


def login(request):
    return render(request, 'Page/login.html')


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        cartItems = order['get_cart_item']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'Page/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId:', productId)
    print('action:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    tansaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['Total'])
        order.Transaction_id = tansaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['Address'],
                city=data['shipping']['City'],
                state=data['shipping']['State'],
                zipcode=data['shipping']['Zipcode']
            )

    else:
        print('User not logged in..')

    return JsonResponse('Process order created', safe=False)
