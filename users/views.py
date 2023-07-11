from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Mandato, Residente, Medicamento, PlanMedicacion, DosisMedicamento, FichaMedica
from .forms import (MandatoForm, ResidenteForm, ResidenteDetailForm,
                    ResidentIngresoEgresoForm, MedicamentoForm, PlanMedicacionForm,
                    DosisMedicamentoForm, PlanMedicacionDetailForm, FichaMedicaForm,
                    FichaMedicaDetailForm
                    )
from .mixins import StaffRequiredMixin, AdministrativoRequiredMixin, EnfermeraRequiredMixin


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


class ResidenteListView(LoginRequiredMixin, StaffRequiredMixin, PermissionRequiredMixin, ListView):
    model = Residente
    template_name = 'users/residente_list.html'
    context_object_name = 'residentes'
    permission_required = 'users.view_residente'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-estado_en_hogar')  # Sort by estado_en_hogar field in descending order
        return queryset

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)


class ResidenteCreateView(LoginRequiredMixin, AdministrativoRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'users/residente_create.html'
    form_class = ResidenteForm
    permission_required = 'users.create_residente'


    def get_success_url(self):
        return reverse("users:users-residente-list")

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)


class ResidenteUpdateView(LoginRequiredMixin, AdministrativoRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'users/residente_update.html'
    form_class = ResidenteForm
    queryset = Residente.objects.all()
    permission_required = 'users.create_residente'

    def get_success_url(self):
        return reverse("users:users-residente-list")

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)

class ResidenteDeleteView(LoginRequiredMixin, AdministrativoRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'users/residente_delete.html'
    queryset = Residente.objects.all()
    permission_required = 'users.create_residente'

    def get_success_url(self):
        return reverse("users:users-residente-list")

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)

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


class ResidenteIngresoEgresoUpdateView(LoginRequiredMixin,  AdministrativoRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'users/residente_ingreso_egreso_update.html'
    form_class = ResidentIngresoEgresoForm
    queryset = Residente.objects.all()
    permission_required = 'users.update_residente'

    def get_success_url(self):
        return reverse("users:users-residente-ingreso-egreso-list")

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)


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


class PlanMedicacionCreateView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'users/planmedicacion_create.html'
    form_class = PlanMedicacionForm
    success_url = reverse_lazy('users:users-planmedicacion-list')
    permission_required = 'users.add_planmedicacion'

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)



class PlanMedicacionUpdateView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'users/planmedicacion_update.html'
    form_class = PlanMedicacionForm
    queryset = PlanMedicacion.objects.all()
    permission_required = 'users.change_planmedicacion'

    def get_success_url(self):
        return reverse("users:users-planmedicacion-list")

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)


class PlanMedicacionDeleteView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = PlanMedicacion
    success_url = reverse_lazy('users:users-planmedicacion-list')
    # Puedes especificar el template_name si deseas utilizar un template personalizado
    permission_required = 'users.delete_planmedicacion'

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)



# Vistas para el modelo DosisMedicamento


class DosisMedicamentoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = DosisMedicamento
    template_name = 'users/dosismedicamentos_list.html'
    context_object_name = 'DosisMedicamentos'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset


class DosisMedicamentoCreateView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'users/dosismedicamentos_create.html'
    form_class = DosisMedicamentoForm
    success_url = reverse_lazy('users:users-dosismedicamento-list')
    permission_required = 'users.add_dosismedicamento'

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)


class DosisMedicamentoUpdateView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'users/dosismedicamentos_update.html'
    form_class = DosisMedicamentoForm
    queryset = DosisMedicamento.objects.all()
    permission_required = 'users.change_dosismedicamento'

    def get_success_url(self):
        dosis_medicamento = self.get_object()
        plan_medicacion_pk = dosis_medicamento.plan_medicacion.pk
        return reverse('users:users-planmedicacion-detail', kwargs={'pk': plan_medicacion_pk})

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)


class DosisMedicamentoDeleteView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = DosisMedicamento
    success_url = reverse_lazy('users:users-dosismedicamento-list')
    permission_required = 'users.delete_dosismedicamento'
    # Puedes especificar el template_name si deseas utilizar un template personalizado

    def get_success_url(self):
        dosis_medicamento = self.get_object()
        plan_medicacion_pk = dosis_medicamento.plan_medicacion.pk
        return reverse('users:users-planmedicacion-detail', kwargs={'pk': plan_medicacion_pk})

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)


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


class DosisMedicamentoResidenteCreateView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, CreateView):
    model = DosisMedicamento
    fields = ['medicamento', 'dosis_diarias', 'hora_administracion']
    template_name = 'users/dosismedicamentos_create.html'
    permission_required = 'users.add_dosismedicamento'

    def form_valid(self, form):
        plan_medicacion = get_object_or_404(PlanMedicacion, pk=self.kwargs['pk'])
        form.instance.plan_medicacion = plan_medicacion
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:users-planmedicacion-detail', kwargs={'pk': self.kwargs['pk']})


# Vistas para el modelo FichaMedica


class FichaMedicaListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = FichaMedica
    template_name = 'users/fichamedica_list.html'
    context_object_name = 'fichasmedicas'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset


class FichaMedicaCreateView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'users/fichamedica_create.html'
    form_class = FichaMedicaForm
    success_url = reverse_lazy('users:users-fichamedica-list')
    permission_required = 'users.add_fichamedica'

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)

class FichaMedicaUpdateView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'users/fichamedica_update.html'
    form_class = FichaMedicaForm
    queryset = FichaMedica.objects.all()
    success_url = reverse_lazy('users:users-fichamedica-list')
    permission_required = 'users.change_fichamedica'

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)





class FichaMedicaDeleteView(LoginRequiredMixin, EnfermeraRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = FichaMedica
    success_url = reverse_lazy('users:users-fichamedica-list')
    permission_required = 'users.delete_fichamedica'

    def handle_no_permission(self):
        try:
            return super().handle_no_permission()
        except PermissionDenied:
            return render(self.request, 'users/permission_denied.html', status=403)






class FichaMedicaDetailView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    template_name = 'users/fichamedica_detail.html'
    model = FichaMedica

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fichamedica = self.get_object()
        form = FichaMedicaDetailForm(instance=fichamedica)
        # Disable editing in the form
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        context['form'] = form
        return context


