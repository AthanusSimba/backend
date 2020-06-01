from rest_framework import serializers
from .models import Farmer


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

        def create(self, validated_data):
            return FarmerSerializer.objects.create(**validated_data)

        def get_objects(self, validated_data):
            return FarmerSerializer.objects.all(validated_data)