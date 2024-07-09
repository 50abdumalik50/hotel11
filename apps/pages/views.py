from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date
from django.views import generic
from django.contrib import messages


from apps.pages.forms import ServiceForm, TeamForm, AboutForm, ContactForm
from apps.pages.models import Service, Team, Facilities, About, Contact
from apps.rooms.models import Room, Booking


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
#     from_date = datetime.strptime(request.POST.get('from'), '%m/%d/%Y').strftime('%Y-%m-%d')
#     to_date = datetime.strptime(request.POST.get('to'), '%m/%d/%Y').strftime('%Y-%m-%d')
#     room = Room.objects.get(id=request.POST.get('number'))
#     # beds = request.POST.get('beds')
#
#     Booking.objects.create(
#         room=room,
#         check_in_date=from_date,
#         check_out_date=to_date,
#         user=request.user,
#     )
#
#     return redirect('/')



def create_booking(request):
    from_date_str = request.POST.get('from')
    to_date_str = request.POST.get('to')

    if from_date_str and to_date_str:
        try:
            from_date = datetime.strptime(from_date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
            to_date = datetime.strptime(to_date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
        except ValueError:
            # Handle the case where date format doesn't match
            # You may want to redirect to an error page or display an error message
            return redirect('/error/')  # Replace '/error/' with your error handling URL

        room_id = request.POST.get('number')
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            # Handle the case where room with given ID doesn't exist
            return redirect('/error/')

        Booking.objects.create(
            room=room,
            check_in_date=from_date,
            check_out_date=to_date,
            user=request.user,
        )

        return redirect('/')
    else:
        # Handle the case where from_date_str or to_date_str is empty
        return redirect('/error/')  # Replace '/error/' with your error handling URL


