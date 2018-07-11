from django.shortcuts import render, redirect

from product.models import Product
from purchase.models import Purchase
from .forms import SignUpForm


def home(request):
    products = Product.objects.filter(quantity__gt=0)
    return render(request, 'core/home.html', {'products': products})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.telephone = form.cleaned_data.get('telephone')
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'core/auth/signup.html', {'form': form})


def create_transaction(request, product_id):
    purchase = Purchase()
    product = Product.objects.get(pk=product_id)
    purchase.product_id = product
    if request.method == 'POST':
        purchase.buyer_name = request.POST.get("name", "")
        purchase.quantity = request.POST.get("quantity", "")
        purchase.buyer_phone_number = request.POST.get("telephone", "")
        purchase.buyer_location = request.POST.get("location", "")
        purchase.product_id = Product.objects.get(pk=product_id)
        purchase.save()
        product.quantity = product.quantity - int(purchase.quantity)
        product.save()
        return redirect('home')
    return render(request, 'core/purchase/create_transaction.html', {'purchase': purchase});