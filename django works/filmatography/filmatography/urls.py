"""
URL configuration for filmatography project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biography.views import MohanlalView
from biography.views import MammoottyView
from biography.views import FahadhView
from biography.views import DulquerView
from biography.views import PrithvirajView
from biography.views import TovinoThomasView
from biography.views import NivinPaulyView
from biography.views import AsifAliView
from biography.views import AntonyVargheseView
from biography.views import AjuVargheseView
from biography.views import NaslenView
from biography.views import ArjunAshokanView
from biography.views import BasilJosephView
from biography.views import SandeepPradeepView
from biography.views import SharafudheenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mohanal/',MohanlalView.as_view()),
    path('mamooty/',MammoottyView.as_view()),
    path('fahaadh/',FahadhView.as_view()),
    path('dulquer/',DulquerView.as_view()),
    path('prithiraj/',PrithvirajView.as_view()),
    path('tovino/',TovinoThomasView.as_view()),
    path('nivin/',NivinPaulyView.as_view()),
    path('asifali/',AsifAliView.as_view()),
    path('antony/',AntonyVargheseView.as_view()),
    path('aju/',AjuVargheseView.as_view()),
    path('naslen/',NaslenView.as_view()),
    path('arjunashokan/',ArjunAshokanView.as_view()),
    path('bj/',BasilJosephView.as_view()),
    path('sandeep/',SandeepPradeepView.as_view()),
    path('sharafudeen/',SharafudheenView.as_view()),
]
