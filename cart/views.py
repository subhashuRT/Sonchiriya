from shop.models import Product
from django.shortcuts import render
# Create your views here.
def cart(request):
    return render(request,'shop/cart.html')
     
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesnotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)

        )
    cart.save( )