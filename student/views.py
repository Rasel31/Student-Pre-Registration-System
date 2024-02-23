from admin_panel.models import CourseListModel, CourseOfferModel
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum, Count
# Create your views here.
from .decorators import student_required
from .models import StudentCourseList
from admin_panel.models import StudentsAdvisorModel


@login_required
@student_required
def register_view(request):
    q = request.POST.get('q')

    query1 = CourseOfferModel.objects.search(q)

    if request.is_ajax():

        course_name = request.GET.get('course_name', False)
        section = request.GET.get('section', False)
        credit = request.GET.get('course_credit', False)

        a = CourseOfferModel.objects.get(course__course_name__iexact=course_name, section__iexact=section)
        d = CourseOfferModel.objects.get(id=a.id)

        enrolled_student = a.enrolled_students
        C = a.course.course_name

        exist_course = StudentCourseList.objects.filter(user=request.user, course__course__course_name=C).exists()

        c_credit = StudentCourseList.objects.filter(user=request.user).aggregate(
            credit=Sum('course__course__course_credit'))
        c_course = StudentCourseList.objects.filter(user=request.user).count()
        print(c_course)
        if c_credit['credit'] is None:
            course_credit = 0 + int(credit)

        else:
            course_credit = c_credit['credit'] + int(credit)

        f = False

        s = StudentsAdvisorModel.objects.get(student=request.user.id)
        student = StudentsAdvisorModel.objects.get(id=s.id)

        if not exist_course and course_credit <= 18 and enrolled_student < 40:
            d.enrolled_students = enrolled_student + 1
            d.save()
            c = StudentCourseList(user=request.user, course=d)
            c.save()
            f = True

            student.number_of_course_taken = c_course + 1
            student.save()
            student.total_credit_taken = course_credit
            student.save()

        data = {
            'is_taken': exist_course,
            'is_save': f,
            'credit': course_credit > 18,
            'enrolled_student': enrolled_student >= 40
        }
        return JsonResponse(data)

    context = {
        'course': query1,
    }
    return render(request, 'course-register.html', context)


@login_required
@student_required
def course_offer_view(request):
    query = CourseListModel.objects.all()

    q = request.POST.get('q1')

    query1 = CourseListModel.objects.search(q)

    semester = request.POST.get('q2')

    course = CourseOfferModel.objects.filter(semester__semester__iexact=semester, section__iexact='A').all()

    context = {
        'search': query,
        'search1': query1,
        'semester': course,
    }

    return render(request, 'course-offer-list.html', context)


@login_required
@student_required
def student_view(request):
    query = StudentCourseList.objects.filter(user=request.user).all()

    context = {
        'course': query
    }
    return render(request, 'student.html', context)
