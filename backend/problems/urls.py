from django.urls import path
from .views import CodingQuestionListAPIView

urlpatterns = [
    path(
        "questions/",
        CodingQuestionListAPIView.as_view(),
        name="coding-question-list",
    ),
]