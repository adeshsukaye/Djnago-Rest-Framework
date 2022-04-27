from django.shortcuts import render
from django.http import JsonResponse
from firstapp.models import Employee

# Create your views here.
def employeeView(request):
    emp = {
        'id' : 123,
        'name' : 'john',
        'sal' : 111111
    }

    data = Employee.objects.all()
    response = {
        'employees':list(data.values('id','name','sal'))
    }
    return JsonResponse(response)
