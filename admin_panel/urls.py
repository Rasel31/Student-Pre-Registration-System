from django.urls import path
from .views import course_offer_view, course_offer_list

app_name = 'admin_panel'

urlpatterns = [

    path('', course_offer_list, name='course-offer-list'),
    path('create', course_offer_view, name='course-offer')

]
