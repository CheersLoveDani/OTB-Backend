from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Hero
from .serializers import HeroSerializer

class HeroListView(APIView):

    def get(self, _request):
        heroes = Hero.objects.all()
        serialized_heroes = HeroSerializer(heroes, many=True)
        return Response(serialized_heroes.data, status=status.HTTP_200_OK)

class HeroDetailView(APIView):
    def get(self, _request, pk):
        try:
            hero = Hero.objects.get(pk=pk)
            serialized_hero = HeroSerializer(hero)
            return Response(serialized_hero.data, status=status.HTTP_200_OK)
        except hero.DoesNotExist:
            raise NotFound()