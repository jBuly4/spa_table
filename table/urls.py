from django.urls import path, re_path
from .views import index_view

urlpatterns = [
    path('', index_view),
    # re_path(r'^/page=[0-9]$', index_view),
]
