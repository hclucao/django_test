from django.urls import path
from . import views

#importanto a funcao index do arquivo views.py e fa
#e depois definir esse arquivo no urls.py dentro do mysite
urlpatterns = [
	path('', views.index, name='index')
]