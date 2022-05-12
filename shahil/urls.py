from django.urls import path,include
from . import views
app_name= 'shahil'

urlpatterns=[
    path('', views.index, name='index'),
    path('message', views.message, name='message'),
]