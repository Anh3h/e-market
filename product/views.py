from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from custom_profile.models import Profile
from product.models import Measurement, Category, Logistic
from purchase.models import Product


def view_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'core/partial/view_product.html', {'product': product})


@login_required
def view_my_products(request):
    products = Product.objects.filter(user_id=request.user.id)
    return render(request, 'core/partial/myproducts.html', {'products': products})


@login_required
def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    measurements = Measurement.objects.all()
    categories = Category.objects.all()
    logistics = Logistic.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get("name", "")
        product.price = request.POST.get("price", "")
        product.quantity = request.POST.get("quantity", "")
        product.measurement_id = Measurement.objects.get(pk=request.POST.get("measurement_id", ""))
        product.category_id = Category.objects.get(pk=request.POST.get("category_id", ""))
        product.logistic_id = Logistic.objects.get(pk=request.POST.get("logistic_id", ""))
        product.description = request.POST.get("description", "")
        product.save()
        return redirect('product:viewProduct', product_id)
    return render(request, 'core/partial/edit_product.html',
                  {'product': product,
                   'measurements': measurements,
                   'logistics': logistics,
                   'categories': categories})


@login_required
def create_product(request):
    product = Product()
    measurements = Measurement.objects.all()
    categories = Category.objects.all()
    logistics = Logistic.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get("name", "")
        product.price = request.POST.get("price", "")
        product.quantity = request.POST.get("quantity", "")
        product.image_link = "link"
        product.user_id = Profile.objects.get(pk=request.user.id)
        product.measurement_id = Measurement.objects.get(pk=request.POST.get("measurement_id", ""))
        product.category_id = Category.objects.get(pk=request.POST.get("logistic_id", ""))
        product.logistic_id = Logistic.objects.get(pk=request.POST.get("logistic_id", ""))
        product.description = request.POST.get("description", "")
        product.save()
        return redirect('product:viewMyProducts')
    return render(request, 'core/partial/create_product.html',
                  {'product': product,
                   'measurements': measurements,
                   'logistics': logistics,
                   'categories': categories})


def delete_product(request, product_id):
    Product.objects.get(pk=product_id).delete()
    return redirect('product:viewMyProducts')
