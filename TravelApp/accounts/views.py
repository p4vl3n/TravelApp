from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views, mixins, get_user_model, login, models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


from TravelApp.accounts.forms import UserRegistrationForm, EditUserProfileForm
from TravelApp.accounts.models import Profile

# Create your views here.
UserModel = get_user_model()


class RestrictedView(mixins.PermissionRequiredMixin, generic.TemplateView):
    template_name = 'home.html'


class RegisterUserView(generic.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('home')


class LogoutUserView(views.LogoutView):
    pass


class EditProfileView(generic.UpdateView):
    model = Profile
    form_class = EditUserProfileForm
    template_name = 'accounts/edit_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile view', kwargs={'pk': self.object.user_id})


class UserProfileView(generic.DetailView):
    model = Profile
    template_name = 'accounts/profile_view.html'
    context_object_name = 'profile'



