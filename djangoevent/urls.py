"""
URL configuration for djangoevent project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Django Event API",
        default_version="v1",
        description="API for Django Event",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("events.urls")),
    path("", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
