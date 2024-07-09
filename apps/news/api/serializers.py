from rest_framework import serializers
from apps.news.models import Post, PostImage, Comment


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


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'created_at',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'post',
            'text',
            'created_at',
            'replay_comment',
        ]

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'user',
            'post',
            'text',
            'replay_comment',
        ]