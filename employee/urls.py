
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from employee import views
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


urlpatterns = [

    # index page route
    path('',views.admin,name='admin'),


    #add employee records  view records and delete records  and edit route
    path('add/',views.add,name='add'),
    path('add/submit/',views.add,name='submit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('view/<int:id>',views.view,name='view'),
    path('edit/<str:id>',views.edit,name='edit'),
    

    #user login routes
    path('login/',views.login,name='login'),
    path('login',views.login,name='login'),

    # user logged out function
    path('logout/',views.logout,name='logout'),
    
    #user register routes
    path('register/',views.register,name='register'),
    path('register/submit/',views.register,name='register'),


    #slider routes
    path('slider/',views.slider,name='slider'),
    path('slider/submit/',views.slider,name='submit-slider'),
    path('slider/delete/<int:id>',views.delslider,name='delete-slider'),
    

]

