from django.urls import path, include

from apps.news import views
from apps.news.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


from apps.news.views import CommentCreateView, CommentDeleteView, CommentListView, CommentDetailView, CommentUpdateView


urlpatterns = [
    path('news/', PostListView.as_view(), name='post_list'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('post/api/', include('apps.posts.api.urls'))


    path('', CommentListView.as_view(), name='index'),
    path('post/<int:post_id>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='detail_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('reply/create/', views.ReplyCreateView.as_view(), name='reply_create'),
    path('reply/<int:reply_id>/update/', views.ReplyUpdateView.as_view(), name='reply_update'),
    path('reply/<int:pk>/delete/', views.ReplyDeleteView.as_view(), name='reply_delete'),

    #
]