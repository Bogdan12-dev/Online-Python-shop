from django.views import View
from django.shortcuts import render
from shop.models import Category, Customer, Product, Cart

def index(request):
    current_user = request.user
    products = Product.objects.all()
    film = Product.objects.filter(category_id=1)
    floor = Product.objects.filter(category_id=2)
    mat = Product.objects.filter(category_id=3)
    thermostat = Product.objects.filter(category_id=6)
    featured = Product.objects.filter(category_id=7)
    categories = Category.objects.all()
    carts = Cart.objects.filter(user_id=current_user.id)

    customer = []
    try:
        customer = Customer.objects.get(user_id=current_user.id)
    except:
        pass
    
    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    params = {
        'customer': customer,
        'products': products,
        'film': film,
        'floor': floor,
        'mat': mat,
        'thermostat': thermostat,
        'featured': featured,
        'categories':categories,
        'qty':qty,
        'total':total,
        'carts':carts,
    }

    return render(request, 'index.html', params)