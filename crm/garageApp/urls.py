from django.conf.urls import url

from .views import AddUser

garage_urls = [
    url('add-user/', AddUser.as_view())
]