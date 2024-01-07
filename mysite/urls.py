from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    #path("")
    path("", include("polls.urls")),
    path("admin/", admin.site.urls),
]
