from django.shortcuts import render
from django.http import JsonResponse
from .models import Bills
# Create your views here.
def IndexView(request):
    obj=Bills.objects.all()
    context={
        "obj":obj,
    }
    return render(request,"index.html",context)
def get_data(request):
    data = Bills.objects.all().values()  
    return JsonResponse(list(data), safe=False)


