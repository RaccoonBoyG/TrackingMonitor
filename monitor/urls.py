from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import upload_from_json

urlpatterns = [
    url(r'upload_json/', upload_from_json, name='upload_from_json'),
]