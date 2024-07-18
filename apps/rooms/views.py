from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View

from django.utils.dateparse import parse_date


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.views import generic
# from django.forms import inlineformset_factory
from datetime import date


from apps.rooms.forms import RoomForm, BookingForm, RoomSearchForm
from apps.rooms.models import Room, Booking


class indexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['rooms'] = Room.objects.all()
    #     print("*"*30)
    #
    #     return context


class RoomListView(generic.ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = "rooms"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = Room.objects.all()
        context['bed'] = Room.objects.all()
        print("*" * 30)

        return context


def create_booking(request):
    from_date = datetime.strptime(request.POST.get('from'), '%m/%d/%Y').strftime('%Y-%m-%d')
    to_date = datetime.strptime(request.POST.get('to'), '%m/%d/%Y').strftime('%Y-%m-%d')
    room = Room.objects.get(id=request.POST.get('number'))
    beds = request.POST.get('beds')

    Booking.objects.create(
        room=room,
        check_in_date=from_date,
        check_out_date=to_date,
        user=request.user,
    )

    return redirect('/')



# def create_booking(request):
#     if request.method == 'POST':
#         number = request.POST.get('number')
#         bed = request.POST.get('bed')
#         if not number or not bed:
#             return HttpResponse( status=400)
#         try:
#             room = Room.objects.get(number=number, bed=bed)
#         except Room.DoesNotExist:
#             return HttpResponse( status=404)
#         booking = Booking(room=room)
#         booking.save()
#         return redirect('booking_success')
#     return render(request, 'rooms.html')
#

class RoomCreateView(generic.CreateView):
    form_class = RoomForm
    model = Room
    success_url = '/'
    template_name = 'room/room_create.html'


class RoomUpdateView(generic.UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'room/room_update.html'
    success_url = '/'

    def form_valid(self, form):
        room = form.save(commit=False)
        room.save()
        return super().form_valid(form)


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = 'room-details.html'
    pk_url_kwarg = 'pk'


class RoomDeleteView(generic.DeleteView):
    model = Room
    pk_url_kwarg = 'pk'
    template_name = 'room/room_delete.html'
    success_url = '/'


class RoomSearchView(View):
    def get(self, request):
        form = RoomSearchForm()
        return render(request, 'room/room_search.html', {'form': form, 'rooms': None})

    def post(self, request):
        form = RoomSearchForm(request.POST)
        if form.is_valid():
            search_number = form.cleaned_data.get('search_number')
            search_type = form.cleaned_data.get('search_type')
            status_choice = form.cleaned_data.get('status_choice')

            rooms = Room.objects.all()

            if search_number:
                rooms = rooms.filter(number=search_number)

            if search_type:
                rooms = rooms.filter(room_type=search_type)

            if status_choice == 'booked':
                rooms = rooms.filter(bookings__isnull=False).distinct()
            elif status_choice == 'available':
                rooms = rooms.filter(bookings__isnull=True).distinct()

            return render(request, 'room/room_search.html', {'form': form, 'rooms': rooms})

        return render(request, 'room/room_search.html', {'form': form, 'rooms': None})




class BookingListView(generic.ListView):
    model = Booking
    template_name = 'rooms.html'
    context_object_name = "bookings"


class BookingUpdateView(generic.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/update.html'
    success_url = reverse_lazy('admin_bookings')

    def form_valid(self, form):
        room = form.save(commit=False)
        room.save()
        messages.success(self.request, 'Booking updated successfully.')
        # Notification.create_notification(self.request.user, f'Ваше бронирование на комнату {room.number} было обновлено.')
        return super().form_valid(form)


class BookingDetailView(generic.DetailView):
    model = Booking
    template_name = 'booking/detail.html'
    pk_url_kwarg = 'pk'


class BookingDeleteView(generic.DeleteView):
    model = Booking
    pk_url_kwarg = 'pk'
    template_name = 'booking/delete.html'
    success_url = reverse_lazy('admin_bookings')



def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    messages.success(request, 'Booking deleted successfully.')

    # Notification.create_notification(self.object.user, f'Ваше бронирование на комнату {self.object.room.number} было удалено.')
    return super().delete(request, *args, **kwargs)



class AdminBookingListView(ListView):
    model = Booking
    template_name = 'booking/admin_list.html'
    context_object_name = 'bookings'
    success_url = reverse_lazy('admin_bookings')


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Booking.objects.filter(
                Q(room__number__icontains=query)
            ).order_by('room__number', 'check_in_date')
        return Booking.objects.all().order_by('room__number', 'check_in_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context


subject = 'Test Email'
message = 'This is a test email sent using SMTP in Django.'
from_email = 'abdumalikabdukarimov50@gmail.com'
recipient_list = ['srojiddin4879@icloud.com']

send_mail(subject, message, from_email, recipient_list)










# class NotificationListView(generic.ListView):
#     model = Notification
#     template_name = 'booking/notifications.html'
#     context_object_name = 'notifications'
#
#     def get_queryset(self):
#         return Notification.objects.filter(user=self.request.user).order_by('-created_at')
#
#     def send_notification(self, user, message):
#         Notification.objects.create(user=user, message=message)
#         send_mail(
#             'Notification from Hotel Booking',
#             message,
#             settings.DEFAULT_FROM_EMAIL,
#             [user.email],
#             fail_silently=False,
#         )
