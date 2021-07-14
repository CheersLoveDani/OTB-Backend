from django.db import models
from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from heroes.serializers import HeroSerializer

User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    dps_1 = HeroSerializer()
    dps_2 = HeroSerializer()
    dps_3 = HeroSerializer()
    
    tank_1 = HeroSerializer()
    tank_2 = HeroSerializer()
    tank_3 = HeroSerializer()

    support_1 = HeroSerializer()
    support_2 = HeroSerializer()
    support_3 = HeroSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'battletag',
            'sr',
            'mainrole',
            'dps_1',
            'dps_2',
            'dps_3',
            'tank_1',
            'tank_2',
            'tank_3',
            'support_1',
            'support_2',
            'support_3',
        )