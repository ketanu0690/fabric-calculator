from django.urls import path,include
from . import views

urlpatterns = [
path('',views.index,name='index'),
path('getdetails/',views.getdetails,name='getdetails'),
path('CostCalculator',views.CostCalculator,name='CostCalculator'),
]