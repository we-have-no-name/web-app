from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('date', 'happy', 'love', 'hopeful', 'neutral', 'angry', 'hopeless', 'hate', 'sad')
