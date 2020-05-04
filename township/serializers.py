from rest_framework import serializers

from .models import State, Township


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Township
        fields = '__all__'
