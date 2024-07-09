from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.news.api import views

router = DefaultRouter()
# router.register.html('', views.CommentViewSet, basename="comment_api")
router.register('', views.PostAPIViewSet, basename="post_api")



urlpatterns = [
    path('comment_crud/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='change'),
    path('comment_create/', views.CommentListCreateView.as_view(), name='comment_create'),
    # path('events/', views.PostListCreateView.as_view(), name='api_post'),
    # path('post/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='api_rud_post'),
    path('post_image/', views.PostImageCreateAPIView.as_view(), name='post_image_create'),
    path('update_image/<int:pk>', views.PostImageUpdateAPIView.as_view(), name='post_image_update'),

]

urlpatterns += router.urls