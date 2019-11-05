from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    path('token-auth/', obtain_jwt_token)
]