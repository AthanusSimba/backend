from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

        def create(self, validated_data):
            return FeedbackSerializer.objects.create(**validated_data)

        def get_objects(self, validated_data):
            return FeedbackSerializer.objects.all(validated_data)
