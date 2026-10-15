from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from .models import CodingQuestion, TestCase, CodeSubmission
from .serializers import (
    CodingQuestionSerializer,
    SampleTestCaseSerializer,
    CodeSubmissionSerializer,
)

class CodingQuestionListAPIView(generics.ListAPIView):
    queryset = CodingQuestion.objects.all().order_by("id")
    serializer_class = CodingQuestionSerializer


class CodingQuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = CodingQuestion.objects.all()
    serializer_class = CodingQuestionSerializer
    lookup_field = "id"

class SampleTestCaseListAPIView(generics.ListAPIView):
    serializer_class = SampleTestCaseSerializer

    def get_queryset(self):
        question_id = self.kwargs["pk"]

        return TestCase.objects.filter(
        question_id=question_id,
        is_sample=True,
        is_hidden=False,
    ).order_by("order")


class CodeSubmissionCreateAPIView(generics.CreateAPIView):
    serializer_class = CodeSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        question_id = self.request.data.get("question")

        if not CodingQuestion.objects.filter(id=question_id).exists():
            raise ValidationError({"question": "Coding question does not exist."})

        serializer.save(user=self.request.user)

class UserSubmissionHistoryAPIView(generics.ListAPIView):
    serializer_class = CodeSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CodeSubmission.objects.filter(
        user=self.request.user
    ).select_related(
        "question"
    ).order_by("-created_at")


