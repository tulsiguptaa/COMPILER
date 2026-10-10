from django.db import models


class CodingQuestion(models.Model):

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default="easy",
    )

    topics = models.JSONField(default=list, blank=True)

    constraints = models.TextField(blank=True)

    starter_code = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TestCase(models.Model):

    question = models.ForeignKey(
        CodingQuestion,
        on_delete=models.CASCADE,
        related_name="test_cases",
    )

    input_data = models.TextField()

    expected_output = models.TextField()

    is_sample = models.BooleanField(default=False)

    is_hidden = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question.title} - Test Case {self.order}"