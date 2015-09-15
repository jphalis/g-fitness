from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse

from marketing.models import Slider
from profiles.models import LessonCount
from schedule.models.events import Event

from .forms import ProfileForm, UserAddressForm
from .models import UserDefaultAddress

# Create your views here.


def home(request):
    sliders = Slider.objects.all_featured()
    context = {'sliders': sliders}
    template = 'home.html'
    return render(request, template, context)


def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)


@login_required
def clients(request):
    client_list = LessonCount.objects.all()
    lesson_set = Event.objects.all()[:1]
    context = {
        "queryset": client_list,
        "lesson_set": lesson_set,
    }
    return render(request, 'clients.html', context)


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        clients = LessonCount.objects.filter(user__username__icontains=q)
        context = {
            'query': q,
            'clients': clients
        }
        template = 'clients.html'
    else:
        context = {}
        template = 'about.html'
    return render(request, template, context)


def workout_schedule(request):
    context = {}
    template = 'workout_schedule.html'
    return render(request, template, context)


def services(request):
    context = {}
    template = 'services.html'
    return render(request, template, context)


def pricing(request):
    context = {}
    template = 'pricing.html'
    return render(request, template, context)


def staff(request):
    context = {}
    template = 'staff.html'
    return render(request, template, context)


def required_forms(request):
    context = {}
    template = 'required_forms.html'
    return render(request, template, context)


def add_user_address(request):
    print request.GET
    try:
        next_page = request.GET.get("next")
    except:
        next_page = None

    form = UserAddressForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.user = request.user
            new_address.save()
            is_default = form.cleaned_data["default"]
            is_default1 = form.cleaned_data["default1"]
            if is_default:
                default_address, created = UserDefaultAddress.objects \
                    .get_or_create(user=request.user)
                default_address.shipping = new_address
                default_address.save()
            if is_default1:
                default_address, created = UserDefaultAddress.objects \
                    .get_or_create(user=request.user)
                default_address.billing = new_address
                default_address.save()
            if next_page is not None:
                return HttpResponseRedirect(reverse(str(next_page)))

    submit_btn = "Save Address"
    form_title = "Add New Address"
    context = {
        'form': form,
        'submit_btn': submit_btn,
        'form_title': form_title
    }
    template = 'form.html'
    return render(request, template, context)


@login_required
def user_profile(request):
    user = None
    lessoncount = LessonCount.objects.get(user=request.user)
    context = {
        'user': user,
        'lessoncount': lessoncount
    }
    return render(request, 'navbar.html', context)


@login_required
def settings(request):
    title = "Account Settings"
    form = ProfileForm(request.POST or None, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.username = request.user.username
            m.save()
            messages.success(
                request, "You have successfully updated your profile.")
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': title,
        'form': form
    }
    template = 'settings.html'
    return render(request, template, context)
