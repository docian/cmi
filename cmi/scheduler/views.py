from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from rest_framework.status import HTTP_200_OK

# Create your views here.
def pacient(request:HttpRequest):
    return HttpResponse(status=200)
