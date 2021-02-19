from django.urls import path

from .views import *

app_name = 'ecommerce'
urlpatterns = [
    path('home/', home_view, name='home'),
    path('tickets/', tickets_view, name='tickets'),
    path('cart/', cart_view, name='buy_ticket')
]
