from django.conf.urls import url
from . import views
from users.views import current_user, UserCreate
from django.urls import path

urlpatterns = [
    url(r'^$', views.UserCreate.as_view(), name='account-create'),
    path('current_user/', current_user)
]
