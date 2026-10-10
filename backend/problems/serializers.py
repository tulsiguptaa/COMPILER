from rest_framework import serializers
from .models import CodingQuestion


class CodingQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CodingQuestion

        fields = [
            "id",
            "title",
            "description",
            "difficulty",
            "topics",
            "constraints",
            "starter_code",
        ]