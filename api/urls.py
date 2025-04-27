from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('hello/', hello_view),
    path('users_list/', user_list),
    path('items_list/', item_list),
    path('post_item/', post_item),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login (get tokens)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 

]