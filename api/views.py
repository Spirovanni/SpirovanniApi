from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import render
from .models import Card, Rating
from .serializers import CardSerializer, RatingSerializer, UserSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action(detail=True, methods=['POST'])
    def rate_card(self, request, pk=None):

        if 'stars' in request.data:
            response = {'message': 'Its working'}
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
