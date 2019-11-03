from rest_framework import serializers
from .models import Olympian

class OlympianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olympian
        fields = ('name', 'team', 'age', 'sport', 'medal')
