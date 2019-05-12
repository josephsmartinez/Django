from django.shortcuts import render
from .forms import ProductForm
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
        prod_list.update(context)

    return render(request, "products/product_detail.html", prod_list)



def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
    'form': form
    }

    return render(request, "products/product_create.html", context)
