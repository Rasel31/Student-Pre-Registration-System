from django.shortcuts import render, redirect
from .forms import CourseOfferForm
from .models import CourseOfferModel
# Create your views here.


def course_offer_view(request):

    if request.method == 'POST':
        form = CourseOfferForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('admin_panel:course-offer-list')
    else:
        form = CourseOfferForm()

    return render(request, 'course_offer.html', {'form': form})


def course_offer_list(request):

    q1 = CourseOfferModel.objects.all()

    context = {
        'course': q1
    }

    return render(request, 'course_offer_list.html', context)
