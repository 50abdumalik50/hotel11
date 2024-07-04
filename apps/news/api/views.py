# DRF
# from rest_framework import viewsets
# from apps.posts.api.serializers import PostCreateSerializer, PostListSerializer, PostSerializer
# from utils.permissions import AdminPermission
# from rest_framework.permissions import IsAdminUser
#


# Serializer class
# class PostAPIViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'create':
#             return PostCreateSerializer
#         elif self.action == 'retrieve':
#             return PostSerializer
#         elif self.action == 'list':
#             return PostListSerializer
#         return PostSerializer
#
#     def get_permissions(self):
#         if self.action in ['create', 'destroy', 'retrieve']:
#             self.permission_classes = [IsAdminUser]
#         else:
#             self.permission_classes = [AdminPermission]
#         return super().get_permissions()