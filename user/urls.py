from django.urls import path

from user.views import *

urlpatterns = [
    path('', user_register_view, name='user_register'),
    path('login/', user_login_view, name='user_login'),
    path('logout/', user_logout_view, name='user_logout')
]
