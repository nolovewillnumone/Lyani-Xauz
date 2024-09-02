from django.urls import path
from . import  views
from .views import reservation_view
from .views import menu_view,MenuDetailView,subscribe






urlpatterns = [
    path('', views.home, name='home'),
    path('base/',views.base, name='base'),
    path('menu/', menu_view, name='menu'),
    path('reservation/', reservation_view, name='reservation'),
    path('location/', views.location, name='location'),
    path('menu/<int:item_id>/', MenuDetailView.as_view(), name='menu_detail'),
    path('subscribe/', subscribe, name='subscribe'),
]




   

