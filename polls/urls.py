from django.urls import path
from . import viwes

#importanto a funcao index do arquivo views.py e fa
urlpatterns = [
	path('', viwes.index, name='index')
]