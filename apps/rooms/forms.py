from django import forms
from django.forms import inlineformset_factory

from apps.rooms.models import Room, Booking


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            # 'Room_choice',
            'room_type',
            'number',
            'number_of_beds',
            'image_for_room',
            'price',

        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'user',
            'room',
            'check_in_date',
            'check_out_date',
            'date_of_reservation',
        ]


class RoomSearchForm(forms.Form):
    search_number = forms.IntegerField(label='Номер комнаты', required=False)
    search_type = forms.ChoiceField(choices=Room.room_choice, label='Тип комнаты', required=False)
    STATUS_CHOICES = [
        ('', 'Any status'),
        ('booked', 'Booked'),
        ('available', 'Available')
    ]
    status_choice = forms.ChoiceField(choices=STATUS_CHOICES, label='Статус', required=False)


# class NotificationForm(forms.ModelForm):
#     class Meta:
#         model = Notification
#         fields = ['user', 'message']
#         widgets = {
#             'user': forms.HiddenInput(),
#             'message': forms.Textarea(attrs={'rows': 3}),
#         }