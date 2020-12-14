from rest_framework import viewsets, status
from django.shortcuts import render
from .models import Card, Rating
from .serializers import CardSerializer, RatingSerializer, UserSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
