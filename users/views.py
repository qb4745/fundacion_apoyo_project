from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView

from .models import Mandato, Residente
from .forms import MandatoForm, ResidenteForm, ResidenteDetailForm
from .mixins import StaffRequiredMixin


class DashBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'



class MandatoView(LoginRequiredMixin, TemplateView):
    template_name = 'users/mandato.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mandatos = Mandato.objects.filter(user=self.request.user)

        if mandatos.exists():
            context["mandatos"] = mandatos
        else:
            context["mandatos"] = None

        return context


class MandatoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'users/mandato_create.html'
    form_class = MandatoForm


    def get_success_url(self):
        return reverse("users:users-mandato")


    def form_valid(self, form):
        form.instance.save(request=self.request)
        return super().form_valid(form)


class MandatoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/mandato_update.html'
    form_class = MandatoForm
    queryset = Mandato.objects.all()

    def get_success_url(self):
        return reverse("users:users-mandato")

    def form_valid(self, form):
        form.instance.save(request=self.request)
        return super().form_valid(form)


class MandatoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'users/mandato_delete.html'
    queryset = Mandato.objects.all()

    def get_success_url(self):
        return reverse("users:users-mandato")


class ResidenteListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Residente
    template_name = 'users/residente_list.html'
    context_object_name = 'residentes'


class ResidenteCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    template_name = 'users/residente_create.html'
    form_class = ResidenteForm


    def get_success_url(self):
        return reverse("users:users-residente-list")


class ResidenteUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = 'users/residente_update.html'
    form_class = ResidenteForm
    queryset = Residente.objects.all()

    def get_success_url(self):
        return reverse("users:users-residente-list")


class ResidenteDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    template_name = 'users/residente_delete.html'
    queryset = Residente.objects.all()

    def get_success_url(self):
        return reverse("users:users-residente-list")

class ResidenteDetailView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    template_name = 'users/residente_detail.html'
    model = Residente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        residente = self.get_object()
        form = ResidenteDetailForm(instance=residente)
        # Disable editing in the form
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context