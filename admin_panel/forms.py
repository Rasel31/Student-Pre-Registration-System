from django import forms
from .models import CourseOfferModel


class CourseOfferForm(forms.ModelForm):

    class Meta:
        model = CourseOfferModel

        fields = [

            'semester',
            'course',
            'section',
            'capacity'
        ]

