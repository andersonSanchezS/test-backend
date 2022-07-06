from rest_framework import serializers
from base.models import cities, divisions, teams, players, matches, positions


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = cities
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = divisions
        fields = '__all__'


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = teams
        fields = '__all__'


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = players
        fields = '__all__'
