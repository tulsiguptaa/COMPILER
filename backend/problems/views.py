from rest_framework import generics

from .models import CodingQuestion
from .serializers import CodingQuestionSerializer


class CodingQuestionListAPIView(generics.ListAPIView):

    queryset = CodingQuestion.objects.all().order_by("id")

    serializer_class = CodingQuestionSerializer