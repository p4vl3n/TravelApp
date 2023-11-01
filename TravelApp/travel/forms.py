from django import forms as django_forms

from TravelApp.accounts.models import Profile
from TravelApp.common.helpers import BootstrapFormMixin
from TravelApp.travel.models import Trip, Image, TripDay


class DateInput(django_forms.DateInput):
    input_type = 'date'


class CreateTripForm(BootstrapFormMixin, django_forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTripForm, self).__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Trip
        fields = '__all__'
        widgets = {
            'departure_date': DateInput(),
            'departure_time': django_forms.TimeInput(attrs={'type': 'time'})
        }


class DeleteTripForm(BootstrapFormMixin, django_forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteTripForm, self).__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Trip
        fields = '__all__'


class FriendSearchForm(django_forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name',
                  'last_name',
                  'country_of_residence',
                  'email',
                  )


class EditDayForm(django_forms.ModelForm):
    class Meta:
        model = TripDay
        fields = ('description', )



