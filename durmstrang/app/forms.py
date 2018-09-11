from django.forms import ModelForm
from django.core.files.images import get_image_dimensions

from durmstrang.app.models import Challenge


class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = [
            "title",
            "description",
            "avatar",
            "reached_points",
            "expected_points",
            "reached_starts",
            "expected_starts",
        ]
