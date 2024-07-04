from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
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

from apps.rooms.forms import RoomForm, BookingForm
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
    template_name = 'room_create.html'


class RoomUpdateView(generic.UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'room_update.html'
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
    template_name = 'room_delete.html'
    success_url = '/'


class BookingListView(generic.ListView):
    model = Booking
    template_name = 'rooms.html'
    context_object_name = "bookings"


class BookingCreateView(generic.CreateView):
    form_class = BookingForm
    model = Booking
    success_url = '/'
    template_name = 'booking/create.html'


class BookingUpdateView(generic.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/update.html'
    success_url = '/'

    def form_valid(self, form):
        room = form.save(commit=False)
        room.save()
        return super().form_valid(form)


class BookingDetailView(generic.DetailView):
    model = Booking
    template_name = 'booking/detail.html'
    pk_url_kwarg = 'pk'


class BookingDeleteView(generic.DeleteView):
    model = Booking
    pk_url_kwarg = 'pk'
    template_name = 'booking/delete.html'
    success_url = '/'









    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['formset'] = inlineformset_factory(Room, Images, form=ImagesForm, extra=self.extra)(
    #             self.request.POST, self.request.FILES, instance=self.object
    #         )
    #     else:
    #         data['formset'] = inlineformset_factory(Room, Images, form=ImagesForm, extra=self.extra)()
    #     return data
    #
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     formset = context['formset']
    #     print(formset)
    #     if formset.is_valid():
    #         self.object = formset.save()
    #         formset.instance = self.object
    #         formset.save()
    #     return super().form_valid(form)




