
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # path('base/', views.base),
    path('about/', views.about),
    path('product/', views.product),
    path('search/<str:keyword>/<int:page>/', views.search),
    path('map/', views.map),
]
