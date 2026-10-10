from django.contrib import admin
from .models import CodingQuestion, TestCase


@admin.register(CodingQuestion)
class CodingQuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "difficulty", "created_at")
    list_filter = ("difficulty",)
    search_fields = ("title", "description")
    ordering = ("-created_at",)


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "order",
        "is_sample",
        "is_hidden",
    )
    list_filter = ("is_sample", "is_hidden")
    search_fields = ("question__title",)
    ordering = ("question", "order")