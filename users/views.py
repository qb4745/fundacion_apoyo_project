from django.shortcuts import render
from django.views.generic import TemplateView


class DashBoardView(TemplateView):
    template_name = 'users/dashboard.html'