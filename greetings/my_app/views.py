from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


class HelloWorldView(View):

    def get(self, request):
        response_data = { "message": "HelloWorld"}

        return JsonResponse(response_data)



class GoodMorningView(View):

    def get(self, request):
        response_data = {"message": "Good Morning"}

        return JsonResponse(response_data) 



class GoodEveningView(View):

    def get(self, request):
        response_data = { "message": "Good Evening"}

        return JsonResponse(response_data)

class GoodAfterNoonView(View):

    def get(self,request):
        response_data={ "message": "Good After Noon"} 

        return JsonResponse(response_data)          