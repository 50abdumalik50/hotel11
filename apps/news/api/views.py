from rest_framework import viewsets, generics
from apps.news.api.serializers import PostCreateSerializer, PostListSerializer, PostSerializer, CommentSerializer, \
    CommentCreateSerializer, PostImageSerializer
from apps.news.models import Post, Comment, PostImage
from utils.permissions import BasePermission
from rest_framework.permissions import IsAdminUser
from utils.permissions import IsAdmin


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        elif self.action == 'retrieve':
            return PostSerializer
        elif self.action == 'list':
            return PostListSerializer
        return PostSerializer


class PostImageCreateAPIView(generics.ListCreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer


class PostImageUpdateAPIView(generics.UpdateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer





class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [BasePermission]
        return super().get_permissions()

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
