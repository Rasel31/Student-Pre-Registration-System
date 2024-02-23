from django.urls import path
from .views import course_offer_view, student_view, register_view

app_name = 'student'

urlpatterns = [

    path('', student_view, name='student-view'),
    path('student/course-offer', course_offer_view, name='course-offer'),
    path('student/course-register', register_view, name='course-register')

]
