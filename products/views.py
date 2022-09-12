from multiprocessing import context
from pickle import NONE
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

# # detailed working
# def product_create_view(request):
#     my_form = RawProductForm()  #it's request.get to see how forms look like
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data) # saving data
#         # else:
#         #     print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)

# Django working
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



def render_initial_data(request):
    iniitial_data = {
        "title": "this is initial title",
        "description": "this is description"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial= iniitial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)

    # one way
    # obj = get_object_or_404(Product, id= my_id)  #throws page not found on invalid id

    # other way
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        "object": obj
    }
    return render(request, "products/product_create.html", context)



def dynamic_delete_view(request, my_id):
    obj = get_object_or_404(Product, id= my_id)
    if request.method == "POST":
        obj.delete()
        return redirect("products/product_create.html") #doubtful why not working
    else:
        print("you are in get method")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)



def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)



def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "desc": obj.description
    # }
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)
