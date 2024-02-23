from django.db import models
import datetime
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from accounts.models import Student, Advisor, User

# Create your models here.


class SemesterListModel(models.Model):

    """ Here admin create semester list with respected year """
    season_choices = (
                  ('Spring', 'Spring'),
                  ('Summer', 'Summer'),
                  ('Fall', 'Fall'),
    )
    season = models.type = models.CharField(max_length=6, choices=season_choices, null=True, blank=True)

    semester = models.CharField(max_length=10, help_text='help: L1T1', null=False, blank=False)

    year_choices = [(r, r) for r in range(2017, datetime.date.today().year + 1)]
    year = models.IntegerField(choices=year_choices, default=datetime.datetime.now().year)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.semester

    class Meta:

        ordering = ['timestamp']


class CourseListModelQueryset(models.query.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(course_name__icontains=query) |
                Q(course_name__iexact=query) |
                Q(course_code__icontains=query) |
                Q(course_code__iexact=query)
            ).all()
        return self.none()


class CourseListModelManager(models.Manager):

    def get_queryset(self):
        return CourseListModelQueryset(self.model, using=self._db)

    def search(self, query):

        return self.get_queryset().search(query)


class CourseListModel(models.Model):

    """ here admin create course name course code and course credit"""

    course_name = models.CharField(max_length=100, blank=False, null=False)
    course_code = models.CharField(max_length=10, blank=False, null=False)
    course_credit = models.IntegerField(default=3)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = CourseListModelManager()

    def __str__(self):
        return self.course_name

    class Meta:

        ordering = ['timestamp']


class CourseOfferModelQueryset(models.query.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(course__course_name__icontains=query) |
                Q(course__course_name__iexact=query) |
                Q(course__course_code__iexact=query) |
                Q(course__course_code__icontains=query)

            ).all()
        return self.none()


class CourseOfferModelManager(models.Manager):

    def get_queryset(self):
        return CourseOfferModelQueryset(self.model, using=self._db)

    def search(self, query):

        return self.get_queryset().search(query)


class CourseOfferModel(models.Model):

    """ here admin create course offer list with semester, course, section, capacity, enrolled students """

    semester = models.ForeignKey(SemesterListModel, on_delete=models.CASCADE, related_name='semesters')
    course = models.ForeignKey(CourseListModel, on_delete=models.CASCADE, related_name='courses')
    section = models.CharField(max_length=1, help_text='Example: A', null=True, blank=True)
    capacity = models.IntegerField(default=40)
    value = 0
    enrolled_students = models.IntegerField(default=value, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = CourseOfferModelManager()

    def get_absolute_url(self):
        return reverse('students:course-details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.course.course_name

    class Meta:
        ordering = ['timestamp']


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=CourseOfferModel)


class StudentsAdvisorModel(models.Model):

    """ Here admin assign student to advisor """

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    number_of_course_taken = models.IntegerField(default=0)
    total_credit_taken = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.user.username

    class Meta:
        ordering = ['-timestamp']

