from django.urls import path
from .views import advisor_view, course_offer_view, register_view

app_name = 'advisor'

urlpatterns = [

    path('', advisor_view, name='advisor-view'),
    path('advisor/course-offer', course_offer_view, name='advisor-course-offer'),
    path('advisor/course-offer/course-register', register_view, name='advisor-course-register')

]
