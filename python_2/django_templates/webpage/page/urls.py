from django.conf.urls import url
from .views import Home

urlpatterns = [
    url("Home",Home.as_view()),
]