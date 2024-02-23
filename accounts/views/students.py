from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from ..models import User
from ..forms import StudentSignUpForm


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Student '
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
