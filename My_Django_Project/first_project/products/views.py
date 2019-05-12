from django.shortcuts import render

from .models import Product
# Create your views here.
def product_detail_view(request):
    #obj =  Product.objects.get(id=1)
    #obj = Product.objects.all()
    prod_list = {}
    for prod in Product.objects.all():
        context = {
        'title': prod.title,
        'description': prod.description
        }
        prod_list.update(context)g

    return render(request, "products/detail.html", prod_list)