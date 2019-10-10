from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Consumo
from django.template import loader

class consumeList(APIView):
    def get(self, request):
        employeesL=Consumo.objects.all()
        mainList=[]
        for employee in employeesL:
            subList=[]
            subList.append(employee.x)
            subList.append(employee.consumo_r)
            subList.append(employee.consumo_s)
            subList.append(employee.consumo_t)
            subList.append(employee.consumo_total)
            mainList.append(subList)
        return Response(mainList)

def getAll(request):
    template="temp/index.html"
    return render(request,template,context={})