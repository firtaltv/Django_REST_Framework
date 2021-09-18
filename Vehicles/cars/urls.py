from django.urls import path, include
from .views import *

urlpatterns = [
    path('create', CarCreateView.as_view()),
    path('all', CarsListView.as_view()),
    path('detail/<int:pk>', CarDetailView.as_view()),
]