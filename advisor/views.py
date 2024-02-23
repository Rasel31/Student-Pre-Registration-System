from accounts.models import User, Advisor
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from admin_panel.models import StudentsAdvisorModel, CourseOfferModel, CourseListModel
# Create your views here.
from student.decorators import advisor_required
from student.models import StudentCourseList


@login_required
@advisor_required
def advisor_view(request):

    qs = StudentsAdvisorModel.objects.filter(advisor=request.user.id)

    queryset = {
        'students': qs
    }

    return render(request, 'advisor.html', queryset)


@login_required
@advisor_required
def course_offer_view(request):
    query = CourseListModel.objects.all()

    q = request.POST.get('q1')

    semester = request.POST.get('q2')

    course = CourseOfferModel.objects.filter(semester__semester__iexact=semester, section__iexact='A').all()

    query1 = CourseListModel.objects.search(q)

    context = {
        'search': query,
        'search1': query1,
        'semester': course,
    }

    return render(request, 'advisor-course-offer-list.html', context)


@login_required
@advisor_required
def register_view(request):
    q = request.POST.get('q')

    b = Advisor.objects.get(user__username=request.user)

    q2 = StudentsAdvisorModel.objects.filter(advisor=b).all()

    query1 = CourseOfferModel.objects.search(q)

    if request.is_ajax():

        course_name = request.GET.get('course_name', False)
        section = request.GET.get('section', False)
        credit = request.GET.get('course_credit', False)
        student = request.GET.get('student', False)

        a = CourseOfferModel.objects.get(course__course_name__iexact=course_name, section__iexact=section)
        d = CourseOfferModel.objects.get(id=a.id)

        enrolled_student = a.enrolled_students
        C = a.course.course_name

        exist_course = StudentCourseList.objects.filter(user__username=student, course__course__course_name=C).exists()

        c_credit = StudentCourseList.objects.filter(user__username=student).aggregate(
            credit=Sum('course__course__course_credit'))

        c_course = StudentCourseList.objects.filter(user__username=student).count()
        print(c_course)

        if c_credit['credit'] is None:
            course_credit = 0 + int(credit)

        else:
            course_credit = c_credit['credit'] + int(credit)

        f = False

        s = User.objects.filter(username=student)
        student = User.objects.get(id=s[0].id)

        if not exist_course and course_credit <= 18 and enrolled_student < 40:

            c = StudentCourseList(user=student, course=d)
            c.save()
            d.enrolled_students = enrolled_student + 1
            d.save()
            f = True

            student_advisor = StudentsAdvisorModel.objects.get(student__user__username=student)
            student_advisor1 = StudentsAdvisorModel.objects.get(id=student_advisor.id)

            student_advisor1.number_of_course_taken = c_course + 1
            student_advisor1.total_credit_taken = course_credit
            student_advisor1.save()

        data = {
            'is_taken': exist_course,
            'is_save': f,
            'credit': course_credit > 18,
            'enrolled_student': enrolled_student >= 40,
        }
        return JsonResponse(data)

    context = {
        'course': query1,
        'student': q2,
    }

    return render(request, 'advisor-course-register.html', context)