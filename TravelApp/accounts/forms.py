from django.contrib.auth import forms as auth_forms, get_user_model, password_validation
from django import forms
from TravelApp.accounts.models import ApplicationUser, Profile
from TravelApp.common.helpers import BootstrapFormMixin
from datetime import date


UserModel = get_user_model()


class UserRegistrationForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            email=self.cleaned_data['email'],
            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ('email',)


class EditUserProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        exclude = ('user_id', 'friends', 'user', 'first_log_in',)

        widgets = {
            'date_of_birth': forms.SelectDateWidget(
                attrs={'class': 'form-control-plaintext'},
                years=[str(year) for year in range(date.today().year, date.today().year - 100, -1)],
            ),
        }

    def save(self, commit=True):
        pass


class UserLoginForm(BootstrapFormMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label


