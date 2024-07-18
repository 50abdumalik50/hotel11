from collections import defaultdict

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import TemplateView

from apps.restaurants.forms import RestaurantForm, HoursForm, RestaurantMenuForm
from apps.restaurants.models import Restaurant, Hour, Restaurant_Menu


class indexView(TemplateView):
    template_name = 'index.html'


class RestaurantMenuListView(generic.ListView):
    model = Restaurant_Menu
    template_name = 'restaurant.html'
    context_object_name = "menus"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grouped_menus = defaultdict(list)
        for menu in Restaurant_Menu.objects.all():
            grouped_menus[menu.menu_type].append(menu)
        context['grouped_menus'] = dict(grouped_menus)
        return context

class RestaurantMenuDetailView(generic.DetailView):
    model = Restaurant_Menu
    template_name = 'restaurant_menu_detail.html'
    pk_url_kwarg = 'pk'

class RestaurantMenuCreateView(generic.CreateView):
    form_class = RestaurantMenuForm
    model = Restaurant_Menu
    success_url = reverse_lazy('restaurant')
    template_name = 'restaurant/restaurant_menu_create.html'


class RestaurantMenuUpdateView(generic.UpdateView):
    model = Restaurant_Menu
    form_class = RestaurantMenuForm
    template_name = 'restaurant/restaurant_menu_update.html'
    success_url = reverse_lazy('restaurant')

    def form_valid(self, form):
        menu_item = form.save(commit=False)
        menu_item.save()
        return super().form_valid(form)

class RestaurantMenuDeleteView(generic.DeleteView):
    model = Restaurant_Menu
    pk_url_kwarg = 'pk'
    template_name = 'restaurant/restaurant_menu_delete.html'
    success_url = reverse_lazy('restaurant')





