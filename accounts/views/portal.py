from django.shortcuts import render, redirect


# Create your views here.
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'signup.html'


def home(request):

    if request.user.is_authenticated:

        if request.user.is_student:
            return redirect('student:student-view')

        elif request.user.is_advisor:
            return redirect('advisor:advisor-view')

    return render(request, 'home.html')
