from django.urls import path
from. import views
urlpatterns = [
    path('second/', views.second_page),
    path('shop/laptop/', views.shop_laptop),
    path('shop/handphone/', views.shop_handphone),
    path('shop/console/', views.shop_console),
    path('firstpage/', views.first_page),
    path('secondpage/', views.second_page),
    path('example/', views.example),
    path('shop/', views.shop),
    path('cobacoba/', views.cobacoba),
    path('shop/laptop/list', views.shop_laptop_list),
    path('coba/list', views.coba_list),
    path('', views.landing_page),
]