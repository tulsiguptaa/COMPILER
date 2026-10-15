from rest_framework import serializers
from .models import CodingQuestion
from .models import CodingQuestion, TestCase,CodeSubmission

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


class CodeSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSubmission
        fields = [
"id",
"question",
"language",
"source_code",
"status",
"passed_test_cases",
"total_test_cases",
"created_at",
]
        read_only_fields = [
"id",
"status",
"passed_test_cases",
"total_test_cases",
"created_at",
]
