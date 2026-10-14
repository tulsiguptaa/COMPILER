from django.urls import path

from .views import (
    CodingQuestionListAPIView,
    CodingQuestionDetailAPIView,
    SampleTestCaseListAPIView
)

urlpatterns = [
    path(
        "questions/",
        CodingQuestionListAPIView.as_view(),
        name="coding-question-list",
    ),
    path(
        "questions/<int:pk>/",
        CodingQuestionDetailAPIView.as_view(),
        name="coding-question-detail",
    ),
    path(
    "questions/<int:pk>/samples/",
    SampleTestCaseListAPIView.as_view(),
    name="sample-test-cases",
),
]