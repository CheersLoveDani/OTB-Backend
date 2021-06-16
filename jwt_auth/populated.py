from django.db import models
from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from heroes.serializers import HeroSerializer

User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    dps1 = HeroSerializer()
    dps2 = HeroSerializer()
    dps3 = HeroSerializer()
    
    tank1 = HeroSerializer()
    tank2 = HeroSerializer()
    tank3 = HeroSerializer()

    support1 = HeroSerializer()
    support2 = HeroSerializer()
    support3 = HeroSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'battletag',
            'sr',
            'mainrole',
            'dps1',
            'dps2',
            'dps3',
            'tank1',
            'tank2',
            'tank3',
            'support1',
            'support2',
            'support3',
        )