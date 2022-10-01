from django.shortcuts import (render,
                              HttpResponseRedirect,
                              get_object_or_404,
                              )
from django.http import (HttpResponse,
                         Http404)
from django.core.exceptions import ObjectDoesNotExist


from .models import Product
from .forms import ProductForm


def index(request):
    return HttpResponse("Hello word, You are in the products index.")


def add_from(request):
    context = {}
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "products/add_product.html", context)


def list_view(request):
    products = Product.objects.all()
    context = {"dataset": products}
    return render(request, "website/products/product_list.html", context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = {"form": form}
    return render(request, "products/update_view.html", context)


def detail_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except ObjectDoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'products/detail.html', {'product': product})


def delete_view(request, product_id):
    context = {}
    try:
        product = Product.objects.get(pk=product_id)
    except ObjectDoesNotExist:
        raise Http404("Product does not exist")

    if request.method == "POST":
        product.delete()
        return HttpResponseRedirect("/")
    return render(request, "products/delete_product.html", context)
