from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello_view),
    path('users_list/', user_list),
    path('items_list/', item_list),
]