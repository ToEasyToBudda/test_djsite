from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable


def crm_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    dct = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table
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
