from django.urls import path
from .views import index, dish


urlpatterns = [
    path('', index, name='index'),
    path('<str:recipe>/', dish, name='dish'),
    ]
