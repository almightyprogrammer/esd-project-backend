from django.urls import path

from .views import (
    hello_view,
    user_list,
    item_list,
    post_item,
    authentication_view,
    paginated_item_view,
    item_page_view,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="ESD Backend API",
        default_version="v1",
        description="API documentation for your app",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # api view for checking everything is allg
    path("hello/", hello_view, name="hello"),

    # basic endpoints for admin purposes
    path("users_list/", user_list, name="users-list"),
    path("items_list/", item_list, name="items-list"),

    # item management
    path("post_item/", post_item, name="post-item"),
    path("items/", paginated_item_view, name="paginated-items"),
    path("item/<int:item_id>/", item_page_view, name="item-detail"),

    # jwt authentication
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # our custom authentication endpoint that wraps the built-in auth system
    path("authentication/", authentication_view, name="custom-auth"),

    # API docs (Swagger UI)
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]