import os
from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth import get_user_model
from utils.image_path import upload_rooms

# from apps.userssss.models import User
User = get_user_model()


class Room(models.Model):
    room_choice = (
        ('Deluxe', 'Deluxe'),
        ('Superior', 'Superior'),
        ('Double', 'Double'),
        ('Junior', 'Suite'),
        ('Family', 'Family'),

    )
    number = models.IntegerField()
    # capacity = models.SmallIntegerField()
    number_of_beds = models.SmallIntegerField()
    room_type = models.CharField(
        max_length=20,
        choices=room_choice,
    )
    image_for_room = models.ImageField(
        upload_to="media/",
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=200,
        decimal_places=2,
    )
    startDate = models.DateField(
        null=True,
    )
    endDate = models.DateField(
        null=True,
    )

    def __str__(self):
        return str(self.number)


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    date_of_reservation = models.DateField(
        default=timezone.now,
    )

    def __str__(self):
        return f" {self.room.number}  {self.user.username} {self.check_in_date} {self.check_out_date} {self.date_of_reservation}"


class Images(models.Model):
    image = models.ImageField(
        upload_to="images/",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="images",
    )


# class RoomImage(models.Model):
#     room = models.ForeignKey(
#         Room, on_delete=models.CASCADE,
#         related_name='gallery_images',
#     )
#     image = models.ImageField(
#         upload_to=upload_rooms,
#     )
#
#     def delete(self, using=None, keep_parents=False):
#         os.remove(self.image.path)
#         super().delete(using=None, keep_parents=False)
#
#     def __str__(self):
#         return f"{self.image.url}"

