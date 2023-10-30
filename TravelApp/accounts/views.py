from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views, mixins, get_user_model, login, models, forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.forms.models import model_to_dict


from TravelApp.accounts.forms import UserRegistrationForm, EditUserProfileForm, UserLoginForm
from TravelApp.accounts.models import Profile

# Create your views here.
UserModel = get_user_model()


class RestrictedView(mixins.PermissionRequiredMixin, generic.TemplateView, generic.RedirectView):
    template_name = 'home.html'

    def get_redirect_url(self, *args, **kwargs):
        print(self.request)
        profile = Profile.objects.get(user_id=self.request.user.id)
        if profile.first_log_in:
            return redirect('edit profile', kwargs={'pk': self.request.user.id})


class RegisterUserView(generic.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    # success_url = reverse_lazy('edit profile')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_success_url(self):
        # pk = self.object.mode
        pk = self.object.id
        a = 5
        return reverse_lazy('edit profile', kwargs={'pk': pk})


def edit_profile(request, pk):
    profile = Profile.objects.get(pk=request.user.id)

    if request.user.pk == profile.pk:
        if request.method == "POST":
            form = EditUserProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                profile.first_log_in = False
                profile.save()
                return redirect('profile view', profile.pk)
        else:
            form = EditUserProfileForm(instance=profile)

        context = {
            'form': form,
            'pk': pk,
            'profile': profile
        }

        return render(request, 'accounts/edit_profile_form.html', context)


class LoginUserView(views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('home')


class LogoutUserView(views.LogoutView):
    pass


class UserProfileView(generic.DetailView):
    model = Profile
    template_name = 'accounts/profile_view.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        profile = Profile.objects.get(user_id=user.id)
        friends = profile.friends.all()
        has_friends = friends.count() > 0
        context['has_friends'] = has_friends
        if has_friends:
            context['friends'] = friends
        return context



