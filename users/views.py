from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Mandato, Residente, Medicamento, PlanMedicacion, DosisMedicamento
from .forms import (MandatoForm, ResidenteForm, ResidenteDetailForm,
                    ResidentIngresoEgresoForm, MedicamentoForm, PlanMedicacionForm,
                    DosisMedicamentoForm, PlanMedicacionDetailForm,
                    )
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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-estado_en_hogar')  # Sort by estado_en_hogar field in descending order
        return queryset


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



class ResidenteIngresoEgresoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Residente
    template_name = 'users/residente_ingreso_egreso.html'
    context_object_name = 'residentes'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-estado_en_hogar')  # Sort by estado_en_hogar field in descending order
        return queryset


class ResidenteIngresoEgresoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = 'users/residente_ingreso_egreso_update.html'
    form_class = ResidentIngresoEgresoForm
    queryset = Residente.objects.all()

    def get_success_url(self):
        return reverse("users:users-residente-ingreso-egreso-list")


from .models import Medicamento, PlanMedicacion, DosisMedicamento

# Vistas para el modelo Medicamento

class MedicamentoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Medicamento
    template_name = 'users/medicamento.html'
    context_object_name = 'medicamentos'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset


class MedicamentoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    template_name = 'users/medicamento_create.html'
    form_class = MedicamentoForm

    def get_success_url(self):
        return reverse("users:users-medicamento-list")


class MedicamentoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = 'users/medicamento_update.html'
    form_class = MedicamentoForm
    queryset = Medicamento.objects.all()

    def get_success_url(self):
        return reverse("users:users-medicamento-list")


class MedicamentoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Medicamento
    success_url = reverse_lazy('users:users-medicamento-list')
    # Puedes especificar el template_name si deseas utilizar un template personalizado


# Vistas para el modelo PlanMedicacion

class PlanMedicacionListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = PlanMedicacion
    template_name = 'users/planmedicacion_list.html'
    context_object_name = 'list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset


class PlanMedicacionCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    template_name = 'users/planmedicacion_create.html'
    form_class = PlanMedicacionForm
    success_url = reverse_lazy('users:users-planmedicacion-list')



class PlanMedicacionUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = 'users/medicamento_update.html'
    form_class = PlanMedicacionForm
    queryset = PlanMedicacion.objects.all()

    def get_success_url(self):
        return reverse("users:users-planmedicacion-list")


class PlanMedicacionDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = PlanMedicacion
    success_url = reverse_lazy('users:users-planmedicacion-list')
    # Puedes especificar el template_name si deseas utilizar un template personalizado



# Vistas para el modelo DosisMedicamento


class DosisMedicamentoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = DosisMedicamento
    template_name = 'users/dosismedicamentos_list.html'
    context_object_name = 'DosisMedicamentos'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset


class DosisMedicamentoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    template_name = 'users/dosismedicamentos_create.html'
    form_class = DosisMedicamentoForm
    success_url = reverse_lazy('users:users-dosismedicamento-list')



class DosisMedicamentoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = 'users/dosismedicamentos_update.html'
    form_class = DosisMedicamentoForm
    queryset = DosisMedicamento.objects.all()
    success_url = reverse_lazy('users:users-dosismedicamento-list')


class DosisMedicamentoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = DosisMedicamento
    success_url = reverse_lazy('users:users-dosismedicamento-list')
    # Puedes especificar el template_name si deseas utilizar un template personalizado


class PlanMedicacionDetailView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    template_name = 'users/planmedicacion_detail.html'
    model = PlanMedicacion
    context_object_name = 'plan_medicacion'  # Singular context name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plan_medicacion = self.object  # Retrieve the PlanMedicacion instance
        dosis_medicamentos = plan_medicacion.dosismedicamento_set.all()  # Retrieve all DosisMedicamento objects
        context['dosis_medicamentos'] = dosis_medicamentos  # Add the dosis_medicamentos to the context
        return context
