from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from TravelApp.accounts.models import ApplicationUser, Profile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.NAME_MAX_LENGTH
    )

    last_name = forms.CharField(
        max_length=Profile.NAME_MAX_LENGTH
    )

    # country_of_residence = forms.ChoiceField(
    #     max_length=25,
    #     choices=Profile.COUNTRY_CHOICES,
    # )

    # gender = forms.CharField(
    #     max_length=35,
    #     choices=Profile.GENDERS,x
    # )

    # date_of_birth = forms.DateField()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'country_of_residence',
            'gender',
            'date_of_birth',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country_of_residence': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
