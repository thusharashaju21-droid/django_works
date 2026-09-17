from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

@method_decorator(csrf_exempt,name="dispatch")
# Create your views here.
class AdditionView(View):
    def post(self,request):
      form_data=loads(request.body) #json native type 
      n1=int(form_data.get("num1"))
      n2=int(form_data.get("num2"))
      result =n1+n2

      response_data={
         
         "message":f"addition of{n1},{n2} = {result}"

      }
      return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class SubstractionView(View):
   def post(self,request):
      form_data=loads(request.body)
      n1=int(form_data.get("num1"))
      n2=int(form_data.get("num2"))
      result=n1-n2

      response_data={
         
         "message":f"substraction of {n1},{n2} = {result}"

      } 
      return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class MultplicationView(View):
   def post(self,request):
      form_data=loads(request.body)
      n1=int(form_data.get("num1"))
      n2=int(form_data.get("num2"))
      result=n1*n2 

      response_data={
         "message":f"multpication of {n1},{n2} = {result}"
      }     

      return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class DivisionView(View):
   def post(self,request):
      form_data=loads(request.body)
      n1=int(form_data.get("num1"))
      n2=int(form_data.get("num2"))
      result=n1/n2

      response_data={
         "message":f"Division of {n1},{n2} = {result}"
      }  

      return JsonResponse(response_data) 

@method_decorator(csrf_exempt,name="dispatch")
class FactorialView(View):
   def post(self,request):
      form_data=loads(request.body) 
      n1=int(form_data.get("num1"))
      fact = 1
      for i in range(1, n1 + 1):
        fact = fact * i
      response_data = {
            "message": f"factorial of {n1} = {fact}"
        }

      return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch") 
class  PrimeView(View):
   def post(self,request):
      form_data=loads(request.body)
      




@method_decorator(csrf_exempt,name="dispatch")
class PerfectView(View):
   def post(self,request):
      form_data=loads(request.body)