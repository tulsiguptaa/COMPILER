from rest_framework import serializers
from .models import CodingQuestion
from .models import CodingQuestion, TestCase

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
class SampleTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = [
"id",
"input_data",
"expected_output",
"order",
]