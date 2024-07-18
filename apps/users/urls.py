from django.urls import path

from apps.users.views import register, CustomLoginView, CustomLogoutView, edit_profile, delete_profile, profile

urlpatterns = [
    path('account/register/', register, name='register'),
    path('account/login/', CustomLoginView.as_view(), name='login'),
    path('account/logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('profile/', profile, name='profile'),  # Добавлен новый маршрут

]





