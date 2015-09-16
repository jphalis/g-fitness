from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse

from profiles.models import LessonCount
from schedule.models.events import Event

from .forms import ProfileForm, UserAddressForm
from .models import UserDefaultAddress

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


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
    return render(request, 'workout_schedule.html', {})


def services(request):
    return render(request, 'services.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def staff(request):
    return render(request, 'staff.html', {})


def required_forms(request):
    return render(request, 'required_forms.html', {})


def add_user_address(request):
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
    return render(request, 'form.html', context)


@login_required
def user_profile(request):
    lessoncount = LessonCount.objects.get(user=request.user)
    return render(request, 'navbar.html', {'lessoncount': lessoncount})


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
    return render(request, 'settings.html', context)
