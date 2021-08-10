from django.urls import path
from. import views
urlpatterns = [
    path('second/', views.second_page),
    path('example/', views.example),
    path('shop/', views.shop),
    path('', views.landing_page),
]