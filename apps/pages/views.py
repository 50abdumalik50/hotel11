from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date
from django.views import generic
from django.contrib import messages
from django.core.exceptions import ValidationError


from apps.pages.forms import ServiceForm, TeamForm, AboutForm, ContactForm

from apps.pages.models import Service, Team, Facilities, About, Contact

from apps.rooms.models import Room, Booking
from core import settings


class ServiceListView(generic.ListView):
    model = Service
    template_name = 'services.html'


class TeamListView(generic.ListView):
    model = Team
    template_name = 'team.html'
    context_object_name = "team"


class TeamCreateView(generic.CreateView):
    form_class = TeamForm
    model = Team
    success_url = reverse_lazy('team')
    template_name = 'team/team_create.html'


class TeamUpdateView(generic.UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'team/team_update.html'
    success_url = reverse_lazy('team')
    def form_valid(self, form):
        room = form.save(commit=False)
        room.save()
        return super().form_valid(form)


class TeamDetailView(generic.DetailView):
    model = Team
    template_name = 'team/team_detail.html'
    pk_url_kwarg = 'pk'


class TeamDeleteView(generic.DeleteView):
    model = Team
    pk_url_kwarg = 'pk'
    template_name = 'team/team_delete.html'
    success_url = reverse_lazy('team')


class FacilitiesListView(generic.ListView):
    model = Facilities
    template_name = 'facilities.html'


class AboutListView(generic.ListView):
    model = About
    template_name = 'about.html'


class ContactListView(generic.ListView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = "contact"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = Room.objects.all()
        context['bed'] = Room.objects.all()
        print("*" * 30)

        return context


# def create_booking(request):
#     from_date_str = request.POST.get('from')
#     to_date_str = request.POST.get('to')
#
#     if from_date_str and to_date_str:
#         try:
#             from_date = datetime.strptime(from_date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
#             to_date = datetime.strptime(to_date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
#         except ValueError:
#             return redirect('/error/')
#
#         room_id = request.POST.get('number')
#         try:
#             room = Room.objects.get(id=room_id)
#         except Room.DoesNotExist:
#             return redirect('/error/')
#
#         Booking.objects.create(
#             room=room,
#             check_in_date=from_date,
#             check_out_date=to_date,
#             user=request.user,
#         )
#
#         return redirect('/')
#     else:
#         return redirect('/error/')


def create_booking(request):
    if request.method == 'POST':
        from_date_str = request.POST.get('from')
        to_date_str = request.POST.get('to')

        if from_date_str and to_date_str:
            try:
                from_date = datetime.strptime(from_date_str, '%m/%d/%Y').date()
                to_date = datetime.strptime(to_date_str, '%m/%d/%Y').date()
            except ValueError:
                return redirect('/error/?message=Invalid date format.')

            room_id = request.POST.get('number')
            try:
                room = Room.objects.get(id=room_id)
            except Room.DoesNotExist:
                return redirect('/error/?message=Room does not exist.')

            stay_duration = (to_date - from_date).days
            if stay_duration < Booking.MIN_STAY_DURATION:
                return redirect(f'/error/?message=The minimum stay duration is {Booking.MIN_STAY_DURATION} days.')

            booking = Booking(
                room=room,
                check_in_date=from_date,
                check_out_date=to_date,
                user=request.user,
            )

            if booking.is_available():
                try:
                    booking.full_clean()
                    booking.save()

                    # Отправка письма после успешного создания бронирования
                    subject = 'Подтверждение бронирования'
                    message = f'Ваше бронирование для комнаты {booking.room.number} с {booking.check_in_date} по {booking.check_out_date} успешно подтверждено!'
                    from_email = 'abdumalikabdukarimov50@gmail.com'
                    recipient_list = [request.user.email]

                    send_mail(subject, message, from_email, recipient_list)

                    return redirect('/')
                except ValidationError as e:
                    errors = e.message_dict.get('__all__', [])
                    return render(request, 'booking_form.html', {'errors': errors, 'rooms': Room.objects.all()})
            else:
                return redirect('/error/?message=The room is not available for the selected dates.')
        else:
            return redirect('/error/?message=Please fill in all required fields.')

    return redirect('/error/?message=Invalid request method.')


# def create_booking(request):
#     if request.method == 'POST':
#         from_date_str = request.POST.get('from')
#         to_date_str = request.POST.get('to')
#
#         if from_date_str and to_date_str:
#             try:
#                 from_date = datetime.strptime(from_date_str, '%m/%d/%Y').date()
#                 to_date = datetime.strptime(to_date_str, '%m/%d/%Y').date()
#             except ValueError:
#                 return redirect('/error/?message=Invalid date format.')
#
#             room_id = request.POST.get('number')
#             try:
#                 room = Room.objects.get(id=room_id)
#             except Room.DoesNotExist:
#                 return redirect('/error/?message=Room does not exist.')
#
#             booking = Booking(
#                 room=room,
#                 check_in_date=from_date,
#                 check_out_date=to_date,
#                 user=request.user,
#             )
#
#             try:
#                 booking.full_clean()
#                 booking.save()
#                 messages.success(request, 'Booking created successfully.')
#                 return redirect('/')
#             except ValidationError as e:
#                 errors = e.message_dict['__all__']
#                 return render(request, 'booking_form.html',
#                               {'errors': errors, 'number': Room.objects.all(), 'bed': Room.objects.all()})
#         else:
#             return redirect('/error/?message=Please fill in all required fields.')
#
#     return redirect('/error/?message=Invalid request method.')






# def create_booking(request):
#     if request.method == 'POST':
#         from_date_str = request.POST.get('from')
#         to_date_str = request.POST.get('to')
#
#         if from_date_str and to_date_str:
#             try:
#                 from_date = datetime.strptime(from_date_str, '%m/%d/%Y').date()
#                 to_date = datetime.strptime(to_date_str, '%m/%d/%Y').date()
#             except ValueError:
#                 return redirect('/error/?message=Invalid date format.')
#
#             room_id = request.POST.get('number')
#             try:
#                 room = Room.objects.get(id=room_id)
#             except Room.DoesNotExist:
#                 return redirect('/error/?message=Room does not exist.')
#
#             booking = Booking(
#                 room=room,
#                 check_in_date=from_date,
#                 check_out_date=to_date,
#                 user=request.user,
#             )
#
#             try:
#                 booking.full_clean()
#                 booking.save()
#                 send_notification(request.user, f'Your booking for room {room.number} has been successfully created.')
#                 return redirect('/')
#             except ValidationError as e:
#                 errors = e.message_dict['__all__']
#                 return render(request, 'booking_form.html', {'errors': errors, 'number': Room.objects.all(), 'bed': Room.objects.all()})
#         else:
#             return redirect('/error/?message=Please fill in all required fields.')
#
#     return redirect('/error/?message=Invalid request method.')
#
# def send_notification(user, message):
#     Notification.objects.create(user=user, message=message)
#     send_mail(
#         'Notification from Hotel Booking',
#         message,
#         settings.DEFAULT_FROM_EMAIL,
#         [user.email],
#         fail_silently=False,
#     )