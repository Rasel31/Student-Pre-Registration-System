from accounts.models import User, Student, Advisor
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import forms


class AdvisorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'first_name',
            'last_name',
            'username'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_advisor = True
        if commit:
            user.save()

        Advisor.objects.create(user=user)
        return user


class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'first_name',
            'last_name',
            'username'
        ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(user=user)
        return user
