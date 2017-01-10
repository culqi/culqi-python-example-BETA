from django.shortcuts import render
from django.http import JsonResponse

from culqipy import culqi

# Create your views here.

def index(request):
    return render(request, 'culqi/index.html')

def charges(request):
    token = request.POST['token']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email =  request.POST['email']
    if request.method == 'POST':
        culqiObject = culqi.Culqi("pk_test_vzMuTHoueOMlgUPj","sk_test_UTCQSGcXW8bCyU59")
        charge = culqiObject.createCharge("Avenida Lima 1232","LIMA",1000,"PE","PEN",email,first_name,0,last_name,"",3333339,"Venta de prueba",token)
        return JsonResponse(charge, safe=False)
    return JsonResponse("only POST method", safe=False)
