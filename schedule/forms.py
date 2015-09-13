from builtins import object
from django import forms
from django.utils.translation import ugettext_lazy as _
from schedule.models import Event, Occurrence


class SpanForm(forms.ModelForm):
    start = forms.DateTimeField(label=_("Start"),
                                widget=forms.SplitDateTimeWidget(date_format='%m/%d/%Y', time_format='%H:%M'))
    end = forms.DateTimeField(label=_("End"),
                              widget=forms.SplitDateTimeWidget(date_format='%m/%d/%Y', time_format='%H:%M'),
                              help_text=_(u"The end time must be later than start time."))

    def clean(self):
        if 'end' in self.cleaned_data and 'start' in self.cleaned_data:
            if self.cleaned_data['end'] <= self.cleaned_data['start']:
                raise forms.ValidationError(_(u"The end time must be later than start time."))
        return self.cleaned_data


class EventForm(SpanForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

    class Meta(object):
        model = Event
        exclude = ('created_on', 'calendar', 'rule', 'end_recurring_period',)


class OccurrenceForm(SpanForm):
    class Meta(object):
        model = Occurrence
        exclude = ('original_start', 'original_end', 'event', 'cancelled')
