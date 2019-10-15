from django.shortcuts import render, HttpResponse, redirect
from apps.Amadon_app.models import *
"""
Product.objects.create(name="Dojo T-shirt", price=19.99)
Product.objects.create(name="Dojo Sweater", price=29.99)
Product.objects.create(name="Dojo Cup", price=4.99)
Product.objects.create(name="Algorithm Book", price=49.99)
"""
def index(request):
    if 'total_amount_bought' in request.session:
        pass
    else:
        request.session['total_amount_bought'] = 0
    if 'total_monye_spent' in request.session:
        pass
    else:
        request.session['total_monye_spent'] = 0.0
    context = {
        "product_list" : Product.objects.all(),
    }
    return render(request,'Amadon_app/index.html',context)
def checkout(request):
    quantity_of_item = int(request.POST.get('quantity'))
    id_of_item = request.POST.get('item_id')
    total_price = Product.objects.get(id=id_of_item).price * float(quantity_of_item)
    request.session['total_amount_bought'] += quantity_of_item
    request.session['total_monye_spent'] += total_price
    context = {
        "total_price" : total_price,
        "amount_total" : request.session['total_amount_bought'],
        "money_total" : request.session['total_monye_spent'],
    }
    return render(request,'Amadon_app/checkout.html',context)
