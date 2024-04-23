from asyncio import Task
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from apps.api.models import Decks, Cards


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decks
        fields = "__all__"

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = "__all__"