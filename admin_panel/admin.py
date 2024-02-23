from django.contrib import admin
from .models import SemesterListModel, CourseListModel, CourseOfferModel, StudentsAdvisorModel
# Register your models here.


class SemesterListAdmin(admin.ModelAdmin):
    list_display = [
        'semester', 'season', 'year'
    ]

    class Meta:
        SemesterListModel


admin.site.register(SemesterListModel, SemesterListAdmin)


class CourseListAdmin(admin.ModelAdmin):

    list_display = [
        'course_name', 'course_code', 'course_credit', 'timestamp'
    ]

    class Meta:
        model = CourseListModel


admin.site.register(CourseListModel, CourseListAdmin)


class CourseOfferAdmin(admin.ModelAdmin):

    list_display = [
        'course', 'semester', 'timestamp', 'section', 'enrolled_students'
    ]

    class Meta:
        model = CourseOfferModel


admin.site.register(CourseOfferModel, CourseOfferAdmin)

admin.site.register(StudentsAdvisorModel)

