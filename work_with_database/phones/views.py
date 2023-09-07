from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):

    sort = request.GET.get('sort')
    if sort == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    else:
        phone_objects = Phone.objects.all()

    template = 'catalog.html'
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_objects = Phone.objects.filter(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone_objects[0]
    }
    return render(request, template, context)
