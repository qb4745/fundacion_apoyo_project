from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from .models import Mandato
from .forms import MandatoForm


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