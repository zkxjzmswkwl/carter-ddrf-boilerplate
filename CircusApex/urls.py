from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework import authtoken
from rest_framework.authtoken import views
from members.views import MemberViewSet

r = routers.DefaultRouter()
r.register(r"members", MemberViewSet)

urlpatterns = [
    path("api/", include(r.urls)),
    path("api/api-token-auth/", views.obtain_auth_token, name="api-token-auth"),
    path("admin/", admin.site.urls),
    path("api-auth/", views.obtain_auth_token),
]
