from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Avg

from .models import Video, Comment
from .serializers import (
    VideoSerializer,
    VideoDetailSerializer,
    VideoCreateSerializer,
    CommentSerializer,
    CommentCreateSerializer,
)


class VideoViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    GET /api/videos/ - List videos (paginated)
    POST /api/videos/ - Create a new video
    GET /api/videos/{id}/ - Video detail
    GET /api/videos/{id}/comments/ - Comments for a video
    POST /api/videos/{id}/comments/ - Add comment to video
    """
    queryset = Video.objects.annotate(comment_count=Count('comments'))

    def get_serializer_class(self):
        if self.action == 'create':
            return VideoCreateSerializer
        if self.action == 'retrieve':
            return VideoDetailSerializer
        if self.action == 'comments':
            return CommentCreateSerializer
        return VideoSerializer

    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, pk=None):
        """GET: List comments. POST: Add a comment."""
        video = self.get_object()

        if request.method == 'POST':
            serializer = CommentCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(video=video)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        comments = video.comments.all()
        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class StatsView(APIView):
    """
    GET /api/stats/ - Engagement statistics
    """
    def get(self, request):
        total_videos = Video.objects.count()
        total_comments = Comment.objects.count()

        most_commented = (
            Video.objects
            .annotate(comment_count=Count('comments'))
            .order_by('-comment_count')[:5]
        )

        recent_videos = Video.objects.order_by('-created_at')[:5]

        avg_comments = (
            Video.objects
            .annotate(comment_count=Count('comments'))
            .aggregate(avg=Avg('comment_count'))
        )

        return Response({
            'total_videos': total_videos,
            'total_comments': total_comments,
            'avg_comments_per_video': round(avg_comments['avg'] or 0, 2),
            'most_commented_videos': [
                {
                    'id': v.id,
                    'title': v.title,
                    'comment_count': v.comment_count,
                }
                for v in most_commented
            ],
            'recent_videos': [
                {
                    'id': v.id,
                    'title': v.title,
                    'created_at': v.created_at,
                }
                for v in recent_videos
            ],
        })
