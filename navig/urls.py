from django.urls import path
from . import views

urlpatterns=[
    path('<course>/<val>',views.course,name='course'),
    path('',views.navig,name='navigate'),
    path('home',views.home,name='home'),
    path('<option>',views.mail,name='mail'),
]
