from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    #path('', views.Home, name='index')
   #path('',views.base),
    path('Login/',views.Login),
    path('Registration/',views.Registation)


]
