import os
import datetime
from datetime import datetime, date


from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError



from utils.image_path import upload_rooms

User = get_user_model()


class Room(models.Model):
    room_choice = (
        ('Deluxe', 'Deluxe'),
        ('Superior', 'Superior'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
        ('Family', 'Family'),

    )
    number = models.IntegerField()
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

    def is_booked(self, check_in_date, check_out_date):
        bookings = Booking.objects.filter(
            room=self,
            check_out_date__gte=check_in_date,
            check_in_date__lte=check_out_date
        )
        return bookings.exists()

    def clean(self):
        if Room.objects.filter(number=self.number).exclude(id=self.id).exists():
            raise ValidationError(f'Room with number {self.number} already exists.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



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
    date_of_reservation = models.DateField(default=timezone.now)

    MIN_STAY_DURATION = 2

    def clean(self):
        today = date.today()

        if self.check_in_date < today or self.check_out_date < today:
            raise ValidationError('Check-in and check-out dates cannot be in the past.')

        if self.check_in_date >= self.check_out_date:
            raise ValidationError('Check-out date must be after check-in date.')

        stay_duration = (self.check_out_date - self.check_in_date).days
        if stay_duration < self.MIN_STAY_DURATION:
            raise ValidationError(f'The minimum stay duration is {self.MIN_STAY_DURATION} days.')

        overlapping_bookings = Booking.objects.filter(
            room=self.room,
            check_out_date__gte=self.check_in_date,
            check_in_date__lte=self.check_out_date
        ).exclude(id=self.id)

        if overlapping_bookings.exists():
            raise ValidationError(f'The room {self.room.number} is already booked for the selected dates.')

    def is_available(self):
        overlapping_bookings = Booking.objects.filter(
            room=self.room,
            check_in_date__lte=self.check_out_date,
            check_out_date__gte=self.check_in_date
        ).exclude(id=self.id)
        return not overlapping_bookings.exists()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Room {self.room.number} booked by {self.user.username} from {self.check_in_date} to {self.check_out_date} on {self.date_of_reservation}"

    @staticmethod
    def get_bookings_by_room():
        return Booking.objects.order_by('room__number', 'check_in_date')

    class Meta:
        ordering = ['-date_of_reservation']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = Room.objects.all()
        context['bed'] = Room.objects.all()
        print("*" * 30)

        return context


# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'Notification for {self.user.username}'

# @staticmethod
# def create_notification(user, message):
#     Notification.objects.create(user=user, message=message)

class Images(models.Model):
    image = models.ImageField(
        upload_to="images/",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="images",
    )


