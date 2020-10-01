from django.db import models

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.models import GhostPost
from backend.serializers import GhostPostSerializer


# Create your views here.
class GhostPostViewSet(viewsets.ModelViewSet):
    queryset = GhostPost.objects.all()
    serializer_class = GhostPostSerializer

    @action(detail=False)
    def boasts(self, request):
        all_boasts = GhostPost.objects.filter(boast_or_roast=True)
        serializer = self.get_serializer(all_boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        all_roasts = GhostPost.objects.filter(boast_or_roast=False)
        serializer = self.get_serializer(all_roasts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = GhostPost.objects.get(id=pk)
        post.up_votes = post.up_votes + 1
        post.save()
        return Response({'upvote': 'You added a vote'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = GhostPost.objects.get(id=pk)
        post.down_votes = post.down_votes - 1
        post.save()
        return Response({'downvote': 'You dropped a vote'})

    @action(detail=False)
    def highestvote(self, request):
        posts = GhostPost.objects.all()
        sorted_posts = sorted(posts, key=lambda p: p.up_votes + p.down_votes, reverse=True)
        serializer = self.get_serializer(sorted_posts, many=True)
        return Response(serializer.data)
