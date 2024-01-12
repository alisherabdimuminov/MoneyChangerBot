from django.urls import path

from .views import card, cards


urlpatterns = [
    path('cards/<int:pk>/', card, name="card"),
    path('cards/', cards, name="cards"),
]
