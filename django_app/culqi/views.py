from django.shortcuts import render
from django.http import JsonResponse

import culqipy

# Create your views here.


def index(request):
    return render(request, 'culqi/index.html')


def charges(request):
    if request.method == 'POST':
        token = request.POST['token']
        installments = request.POST['installments']

        culqipy.API_KEY = "sk_test_UTCQSGcXW8bCyU59"

        dir_charge = {'amount': 3500,
                      'capture': True,
                      'currency_code': 'PEN',
                      'description': 'Culqi Store',
                      'email': 'wmuro@me.com',
                      'installments': installments,
                      'metadata': {'order_id': '1234'},
                      'source_id': token}

        charge = culqipy.Charge.create(dir_charge)

        return JsonResponse(charge, safe=False)

    return JsonResponse("only POST method", safe=False)
