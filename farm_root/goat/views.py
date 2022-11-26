from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, FormView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.db.models import ProtectedError

from .models import Buck, Doe, Photo
from .forms import DoeForm, BuckForm, DoeImagesFormset, BuckImagesFormset

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                    self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

class HerdListView(ListView):
    template_name = 'goat/herd_list.html'
    context_object_name = 'goats'

    def get_queryset(self):
        queryset = {'bucks': Buck.objects.filter(status='BREEDER'),
                    'does': Doe.objects.filter(status='BREEDER'),
                    'bucklings': Buck.objects.filter(status='KID', availability='NO'),
                    'doelings': Doe.objects.filter(status='KID', availability='NO'),}
        return queryset


class SaleListView(ListView):
    template_name = 'goat/sale_list.html'
    context_object_name = 'goats'

    def get_queryset(self):
        queryset = {'bucklings': Buck.objects.exclude(availability='NO'),
                    'doelings': Doe.objects.exclude(availability='NO'),}
        return queryset

class PastListView(ListView):
    template_name = 'goat/past_list.html'
    context_object_name = 'goats'

    def get_queryset(self):
        queryset = {'bucklings': Buck.objects.filter(status='SOLD'),
                    'doelings': Doe.objects.filter(status='SOLD'),}
        return queryset

class RetiredListView(ListView):
    template_name = 'goat/retired_list.html'
    context_object_name = 'goats'

    def get_queryset(self):
        queryset = {'bucks': Buck.objects.filter(status='RETIRED'),
                    'does': Doe.objects.filter(status='RETIRED'),}
        return queryset

class BuckCreateView(UserAccessMixin, CreateView):
    permission_required = 'goat.add_goat'
    model = Buck
    template_name = 'goat/buck_create.html'
    form_class = BuckForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Buck has been added.'
        )
        return super().form_valid(form)

class DoeCreateView(UserAccessMixin, CreateView):
    permission_required = 'goat.add_goat'
    model = Doe
    template_name = 'goat/doe_create.html'
    form_class = DoeForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Doe has been added.'
        )
        return super().form_valid(form)

class BuckDetailView(DetailView):
    model = Buck
    template_name = 'goat/buck_detail.html'

class DoeDetailView(DetailView):
    model = Doe
    template_name = 'goat/doe_detail.html'

class DoeImagesUpdateView(UserAccessMixin, SingleObjectMixin, FormView):
    permission_required = 'photo.add_photo'
    model = Doe
    template_name = 'goat/doe_image_update.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Doe.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Doe.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return DoeImagesFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Changes were saved."
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.get_absolute_url()

class BuckImagesUpdateView(UserAccessMixin, SingleObjectMixin, FormView):
    permission_required = 'photo.add_photo'
    model = Buck
    template_name = 'goat/buck_image_update.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Buck.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Buck.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return BuckImagesFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Changes were saved."
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.get_absolute_url()

class DoeUpdateView(UserAccessMixin, UpdateView):
    permission_required = 'doe.edit_doe'
    model = Doe
    template_name = 'goat/doe_update.html'
    form_class = DoeForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Doe has been updated.'
        )
        return super().form_valid(form)

class BuckUpdateView(UserAccessMixin, UpdateView):
    permission_required = 'buck.update_buck'
    model = Buck
    template_name = 'goat/buck_update.html'
    form_class = BuckForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Buck has been updated.'
        )
        return super().form_valid(form)

class DoeDeleteView(UserAccessMixin, DeleteView):
    permission_required = 'doe.delete_doe'
    model = Doe
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.add_message(
                self.request,
                messages.WARNING,
                "Doe can't be deleted. Delete descendant first."
            )
            return self.form_invalid(form)

class BuckDeleteView(UserAccessMixin, DeleteView):
    permission_required = 'buck.delete_buck'
    model = Buck
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.add_message(
                self.request,
                messages.WARNING,
                "Buck can't be deleted. Delete descendant first."
            )
            return self.form_invalid(form)
