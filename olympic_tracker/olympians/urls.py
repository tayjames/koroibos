from django.conf.urls import url
from . import views

urlpatterns = [
    url(
    r'^api/v1/olympians',
    views.get_olympians,
    name='get_olympians'
    )
]
