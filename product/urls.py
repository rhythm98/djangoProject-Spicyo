from django.urls import path

from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('addResult',views.addResult,name='addResult')
]