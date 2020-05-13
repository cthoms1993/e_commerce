from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_cart(request):
    """a view that redners thw cart"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """a view that adds a quantitiy of specific products to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """used to adjust the quantitiy of a specified product tp specified amount"""
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
