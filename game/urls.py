from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

app_name = "game"

urlpatterns = [
    path("api/doc", SpectacularAPIView.as_view(), name="doc"),
    path(
        "api/doc/swagger",
        SpectacularSwaggerView.as_view(url_name="doc"),
        name="swagger-ui",
    ),
    path(
        "api/doc/redoc",
        SpectacularRedocView.as_view(url_name="doc"),
        name="redoc",
    ),
]
