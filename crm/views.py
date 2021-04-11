from django.shortcuts import render
from .models import Order
from .forms import OrderForm

def crm_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    dct = {
        'object_list': object_list,
        'form': form
    }
    return render(request, './index.html', dct)

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    data = {
        'name': name,
        'phone': phone
    }
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thanks_page.html', data)
