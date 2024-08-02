from django.urls import path
from .views import index

urlpatterns = [
    # Other URL patterns if you have additional views
    path('sats/', index, name='convert'),
]

