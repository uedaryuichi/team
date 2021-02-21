from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class HomeView(TemplateView):
    template_name = "user/index.html"
