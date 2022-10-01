from django.shortcuts import render



def homepage_view(request, *args, **kwargs):
    context = {}
    context['webpage'] = "Factoria"
    return render(request, "base.html", context)

def products_view(request, *args, **kwargs):
    context = {}
    context['webpage'] = "Factoria"
    return render(request, "website/products/product_list.html", context)
