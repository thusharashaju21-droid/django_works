from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from django.http import JsonResponse
from django.views.generic import View
from django.http import JsonResponse

class MohanlalView(View):
    def get(self,request):
        response_data={
            "name":"Mohanlal",
            "language":"Malayalam",
            "film":"Lucifer"
        }
        return JsonResponse(response_data)

class MammoottyView(View):
    def get(self,request):
        response_data = {
            "name":"Mammootty",
            "language":"Malayalam",
            "film":"Bheeshma Parvam"
        }
        return JsonResponse(response_data)

class FahadhView(View):
    def get(self, request):
        response_data = {
            "name": "Fahadh Faasil",
            "language": "Malayalam",
            "film":"Kumbalangi Nights"
        }
        return JsonResponse(response_data)

class DulquerView(View):
    def get(self, request):
        response_data = {
            "name": "Dulquer Salmaan",
            "language": "Malayalam",
            "film": "Bangalore Days"
        }
        return JsonResponse(response_data)

class PrithvirajView(View):
    def get(self, request):
        response_data = {
            "name": "Prithviraj Sukumaran",
            "language": "Malayalam",
            "film":"Driving Licence"
        }
        return JsonResponse(response_data)

class TovinoThomasView(View):
    def get(self,request):
        response_data={"name":"Tovino Thomas",
                       "language":"Malayalam",
                       "film":"Maradona"
        }
        return JsonResponse(response_data)

class NivinPaulyView(View):
    def get(self,request):
        response_data={"name":"Nivin Pauly",
                       "language":"Malayalam",
                       "film":"Bethelem Kudumbha Unit"
        }               
        return JsonResponse(response_data)


class AsifAliView(View):
    def get(self, request):
        response_data = {"name": "Asif Ali", 
                         "language": "Malayalam",
                        "film":"Anuraga Karikkin Vellam"
        }
        return JsonResponse(response_data)  


class AntonyVargheseView(View):
    def get(self, request):
        response_data = {"name": "Antony Varghese", 
                         "language": "Malayalam",
                        "film":"Angamaly Diaries"
        }
        return JsonResponse(response_data)

class AjuVargheseView(View):
    def get(self, request):
        response_data = {"name": "Aju Varghese", 
                         "language": "Malayalam", 
                         "film":"Thattathin Marayathu"
        }
        return JsonResponse(response_data)  

class NaslenView(View):
    def get(self, request):
        response_data = {"name": "Naslen", 
                         "language": "Malayalam", 
                         "film": "Premalu"
        }
        return JsonResponse(response_data)

class ArjunAshokanView(View):
    def get(self, request):
        response_data = {"name": "Arjun Ashokan",
                          "language": "Malayalam", 
                          "films":"Thalavara"
        }
        return JsonResponse(response_data)

class BasilJosephView(View):
    def get(self, request):
        response_data = {"name": "Basil Joseph",
                        "language": "Malayalam", 
                        "film":"Minnal Murali"
        }
        return JsonResponse(response_data)


class SandeepPradeepView(View):
    def get(self, request):
        response_data = {"name": "Sandeep Pradeep", 
                         "language": "Malayalam", 
                         "film": "Padakkalam"
        }                
        return JsonResponse(response_data)    

class SharafudheenView(View):
    def get(self, request):
        response_data = {"name": "Sharafudheen", 
                         "language": "Malayalam", 
                         "film":"Anjam Pathira"
        }
        return JsonResponse(response_data)   
        
    