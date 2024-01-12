from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Card


@api_view(http_method_names=["GET", "POST"])
def cards(request):
    cards = Card.objects.all()
    data = []
    print(cards)
    for i in cards:
        allowed_cards = []
        for j in i.allowed_cards.all():
            allowed_cards.append({
                "name": j.name,
                "validator": j.validator,
                "example": j.example,
            })
        data.append({
            "id": i.pk,
            "name": i.name,
            "validator": i.validator,
            "example": i.example,
            "allowed_cards": allowed_cards
        })
    return Response(data=data)
    # return Response({})

@api_view(http_method_names=['GET', 'POST'])
def card(request, pk):
    card = Card.objects.get(pk=pk)
    allowed_cards = []
    for j in card.allowed_cards.all():
        allowed_cards.append({
            "name": j.name,
            "validator": j.validator,
            "example": j.example,
        })
    data = {}
    data["id"] = card.pk
    data["name"] = card.name
    data["validator"] = card.validator
    data["example"] = card.example
    data["allowed_cards"] = allowed_cards
    return Response(data=allowed_cards)

def home(request):
    return render(request, "index.html", {
        
    })
