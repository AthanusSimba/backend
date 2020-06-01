from rest_framework import serializers
from .models import Faqs


class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = '__all__'

        def create(self, validated_data):
            return FaqsSerializer.objects.create(**validated_data)

        def get_objects(self, validated_data):
            return FaqsSerializer.objects.all(validated_data)