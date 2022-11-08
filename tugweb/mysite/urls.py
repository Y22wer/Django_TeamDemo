from django.contrib import admin
from django.urls import path,include
from mysite import views
urlpatterns = [
    #(r'^icon.png$','django.views.generic.simple.redirect_to',{'url':'/static/images/icon.png'}),
    path('', views.index),
    path('chart/', views.chart),
    path('introduce/', views.introduce),
    path('ship_sign/', views.ship_sign),

    path('show/', views.show_class.as_view()),
    #path('show/', views.show),
    
    path('admin/', admin.site.urls),
]