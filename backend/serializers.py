from rest_framework import serializers

from backend.models import GhostPost


class GhostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhostPost
        fields = [
            'boast_or_roast',
            'post',
            'up_votes',
            'down_votes',
            'submission_time'
        ]
