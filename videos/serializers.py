from rest_framework import serializers
from .models import Video, Comment
from .generator import generate_video_id, generate_video_url


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']
        read_only_fields = ['created_at']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']


class VideoSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'created_at', 'comment_count']
        read_only_fields = ['id', 'created_at']


class VideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'created_at']
        read_only_fields = ['id', 'url', 'created_at']

    def create(self, validated_data):
        video_id = generate_video_id()
        validated_data['id'] = video_id
        validated_data['url'] = generate_video_url(video_id)
        return super().create(validated_data)


class VideoDetailSerializer(VideoSerializer):
    """Same as VideoSerializer - comments available via /videos/{id}/comments/"""
    pass
