from django.contrib import admin
from .models import CodingQuestion, TestCase, CodeSubmission


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

@admin.register(CodeSubmission)
class CodeSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "question",
        "language",
        "status",
        "created_at",
    )

    list_filter = ("language", "status")
    search_fields = ("user__username", "question__title")
    ordering = ("-created_at",)