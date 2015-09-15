from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm

# Create your views here.


def home(request):
    title = "Contact G Fitness"
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        sender = form.cleaned_data['email']
        received_message = form.cleaned_data['message']
        subject = 'Message from G Fitness Contact Form'
        sent_message = '{} {}'.format(received_message, name)
        to_us = [settings.EMAIL_HOST_USER]
        send_mail(subject, sent_message, sender,
                  to_us, fail_silently=True)
        title = 'Thank you'
        confirm_message = """
        Thank you for your message. We have received it, and we are reviewing it.
        """
        form = None

    context = {
            'title': title,
            'form': form,
            'confirm_message': confirm_message
    }
    return render(request, 'contact.html', context)
