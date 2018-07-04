from django.shortcuts import render

from purchase.models import Products


def view_product(request, product_id):
    product = Products.objects.get(pk=1);
    return render(request, 'core/partial/view_product.html', {'product': product})
