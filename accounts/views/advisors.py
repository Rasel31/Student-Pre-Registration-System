from accounts.forms import AdvisorSignUpForm
from accounts.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView


class AdvisorSignUpView(CreateView):
    model = User
    form_class = AdvisorSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Teacher '
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
