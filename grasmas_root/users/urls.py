
from django.conf.urls import url, include

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
]
