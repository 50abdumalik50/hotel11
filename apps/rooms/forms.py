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
            'startDate',
            'endDate',
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


# class ImagesForm(forms.ModelForm):
#     class Meta:
#         model = RoomImage
#         fields = ('image',)
#         widgets = {'image': forms.ClearableFileInput(attrs={
#                                             'class': 'form-control'
#         })}
#
#
# RoomImagesFormSet = inlineformset_factory(Room, Images, form=ImagesForm, extra=1, max_num=5)