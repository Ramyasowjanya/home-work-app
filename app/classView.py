from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework import request

from app.models import *
from django.views.generic import *
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class RestaurantList(ListView):
    model = Restaurant

@method_decorator(login_required,name="dispatch")
class RestaurantDetail(ListView):
    model = Restaurant
    template_name = 'app/restaurant_detail.html'

    def get_context_data(self, **kwargs):
            context = super(RestaurantDetail, self).get_context_data(**kwargs)
            context['x']=Restaurant.objects.filter(user__username__exact=self.request.user)
            return context
    def get_queryset(self):
        user = self.request.user
        return Restaurant.objects.filter(user__username=user)

class MenuList(ListView):
    model=Menus

    def get_context_data(self, **kwargs):
        context = super(MenuList, self).get_context_data(**kwargs)
        h = self.kwargs.get('pk')
        context['hotel']=h
        context['menus_list']=Menus.objects.all().filter(hotel__id=h)
        return context

    def get_queryset(self):
        h = self.kwargs.get('pk')
        return Menus.objects.all().filter(hotel__id=h)


@method_decorator(login_required,name="dispatch")
# class MenuDetail(DetailView):
#     model=Menus
#     template_name = 'app/menus_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MenuDetail, self).get_context_data(**kwargs)
#         try:
#             if Menus.objects.filter(hotel__id=self.kwargs.get('pk'))==[]:
#                 raise Exception('I know Python!')
#             context['menus_detail'] = Menus.objects.filter(hotel__id=self.kwargs.get('pk'))
#         except Exception:
#             context['menus_detail']=[]
#         context['id'] = self.kwargs.get('pk')
#         return context
class MenuDetail(ListView):
    model=Menus

    template_name = 'app/menus_detail.html'
 #   success_url="menulist"
    def get_context_data(self, **kwargs):
        context = super(MenuDetail, self).get_context_data(**kwargs)
        user = self.request.user
        r=Restaurant.objects.filter(user__username=user)
        context['menus_detail'] = Menus.objects.filter(hotel=r)
        return context
    def get_queryset(self):
            user=self.request.user
            r=Restaurant.objects.filter(user__username=user)
            return Menus.objects.filter(hotel=r)

@method_decorator(login_required,name="dispatch")
class RestaurantCreateView(CreateView):
    model=Restaurant
    fields=['name','location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('loginlist')

@method_decorator(login_required,name="dispatch")
class MenuCreateView(CreateView):
    model=Menus
    fields=['name','cost']
    template_name = 'app/menu_form.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.hotel = Restaurant.objects.get(user__username=user)
        return super(MenuCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('menulist')

@method_decorator(login_required,name="dispatch")
class RestauarntUpdateView(UpdateView):
    model=Restaurant
    fields = ('name', 'location',)

    def get_object(self, queryset=None):
        return Restaurant.objects.get(user__username=self.request.user)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestauarntUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('menulist')

@method_decorator(login_required,name="dispatch")
class MenuUpdateView(UpdateView):
    model=Menus
    template_name = 'app/menu_form.html'
    fields = ('name', 'cost',)

    def form_valid(self, form):
        user = self.request.user
        form.instance.hotel = Restaurant.objects.get(user__username__exact=user)
        return super(MenuUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('menulist')

@method_decorator(login_required,name="dispatch")
class MenuDelete(DeleteView):
    model=Menus
    success_url = reverse_lazy("menulist")


