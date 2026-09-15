from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from django.http import JsonResponse

class MohanalView(View):
    def get(self,request):
        response_data={
            "name":"Mohanal",
            "language":"Malayalam",
            "films": "680"
        }

        return JsonResponse(response_data)