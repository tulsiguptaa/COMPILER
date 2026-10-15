from django.urls import path

from .views import (
    CodingQuestionListAPIView,
    CodingQuestionDetailAPIView,
    SampleTestCaseListAPIView,
    CodeSubmissionCreateAPIView,
    UserSubmissionHistoryAPIView
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
path(
    "submissions/",
    CodeSubmissionCreateAPIView.as_view(),
    name="create-submission",
),
path(
    "submissions/history/",
    UserSubmissionHistoryAPIView.as_view(),
    name="submission-history",
),
]