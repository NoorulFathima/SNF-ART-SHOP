from django.urls import path
from . import views


urlpatterns = [
    path('', views.top, name='top'),
    path('Pencil_art/', views.pencil_art, name='Pencil_art'),
    path('Watercolor/', views.watercolor, name='Watercolor'),
    path('Digital_art/', views.digital_art, name='Digital_art'),
    path('cart/', views.cart, name='cart'),
    path('like/', views.like, name='like'),
    path('login/', views.login, name='login'),
]
