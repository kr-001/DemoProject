from . import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
     path('' , views.index,name='index'),
     path('register' , views.register , name='register'),
     path('works/<str:work_type>/', views.work_by_type, name='works_by_type'),
     path('works/', views.work, name='all_works'),
     path('/searchItems',views.search , name='searchItems'),

]
