# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from produtos.forms import ProductForm
from produtos.models import Product


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


@login_required
def product_new(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'product_form.html', {'form': form})


@login_required
def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'product_form.html', {'form': form})


@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'product_delete_confirm.html', {'product': product})
