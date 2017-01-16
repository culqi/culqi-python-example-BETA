from django.shortcuts import render
from django.http import JsonResponse

import culqipy

# Create your views here.

def index(request):
    return render(request, 'culqi/index.html')

def charges(request):
    token = request.POST['token']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email =  request.POST['email']
    if request.method == 'POST':
        culqipy.API_KEY = "sk_test_UTCQSGcXW8bCyU59"
        charge = culqipy.Charge.create(
          address="Avenida Lima 1232",
          address_city="LIMA",
          amount=1000,
          country_code="PE",
          currency_code="PEN",
          email=email,
          first_name=first_name,
          installments=0,
          last_name=last_name,
          metadata="",
          phone_number=3333339,
          product_description="Venta de prueba",
          token_id=token)
        return JsonResponse(charge, safe=False)
    return JsonResponse("only POST method", safe=False)
