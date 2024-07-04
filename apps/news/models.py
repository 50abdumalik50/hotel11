from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    # image_for_news = models.ImageField(
    #     upload_to="media/",
    #     blank=True,
    #     null=True,
    # )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.title}'


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='PostImage'

    )
    image=models.ImageField(
        verbose_name='Изображение',
        upload_to='post_images/'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Изображение для {self.post.title}'


class Comment(models.Model):
    related_name="comments"
    # room = models.ForeignKey(
    #     Room,
    #     on_delete=models.CASCADE,
    #     related_name="comments",
    # )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.CharField(
        max_length=500,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    replay_comment = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='replies',
        null=True,
        blank=True,
    )



    def __str__(self):
        return f"{self.user} - {self.text}"
