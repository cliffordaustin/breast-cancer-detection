"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views import View
import os
from django.http import FileResponse


class VerificationFileView(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(
            settings.STATIC_ROOT,
            ".well-known",
            "pki-validation",
            "A2CA7BA8E8B33D1FC45CB4BCB80E6DE3.txt",
        )
        return FileResponse(open(file_path, "rb"))


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", include("prediction.api.urls")),
    path("api/v1/rest-auth/", include("dj_rest_auth.urls")),
    path("api/v1/rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/rest-auth/password/change/", include("dj_rest_auth.urls")),
    path("api/v1/rest-auth/logout/", include("dj_rest_auth.urls")),
    path("accounts/", include("allauth.urls")),
    path(
        ".well-known/pki-validation/A2CA7BA8E8B33D1FC45CB4BCB80E6DE3.txt",
        VerificationFileView.as_view(),
        name="pki-validation",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
