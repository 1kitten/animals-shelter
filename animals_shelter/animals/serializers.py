from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    """
    Serializer for Animal model.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Animal
        fields = [
            'name',
            'age',
            'arrival_date',
            'weight',
            'height',
            'additional_information',
            'user'
        ]
