from rest_framework import serializers
from apps.posts.models import Post, PostImage


class PostCreateSerializer(serializers.ModelSerializer):
    # create post serializer
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
        ]


class PostListSerializer(serializers.ModelSerializer):
    # List Post serializer
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'created_at',
        ]