from rest_framework import generics
from .models import CodingQuestion, TestCase
from .serializers import CodingQuestionSerializer, SampleTestCaseSerializer


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