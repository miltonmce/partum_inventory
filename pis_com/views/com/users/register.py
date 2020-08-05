from django.views.generic import FormView
from django.contrib.auth import forms as auth_forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from pis_retailer.forms import RetailerForm, RetailerUserForm
from pis_retailer.models import RetailerUser
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


class RegisterView(FormView):
    form_class = auth_forms.UserCreationForm
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # register new user in the system
        user = form.save()

        # Create Retailer
        retailer_form_kwargs = {
            'name': (
                '%s %s' % (user.first_name, user.last_name) if
                user.first_name else user.username),
            'slug': (
                '%s-%s' % (user.first_name, user.last_name) if
                user.first_name else user.username)
        }
        retailer_form = RetailerForm(retailer_form_kwargs)
        if retailer_form.is_valid():
            retailer = retailer_form.save()

            retailer_user_kwargs = {
                'retailer': retailer.id,
                'user': user.id,
                'role_type': RetailerUser.ROLE_TYPE_LEDGER_VIEW
            }

            retailer_user_form = RetailerUserForm(retailer_user_kwargs)
            if retailer_user_form.is_valid():
                retailer_user_form.save()

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        auth_user = authenticate(username=username, password=raw_password)
        auth_login(self.request, auth_user)

        return HttpResponseRedirect(reverse('ledger:customer_ledger_list'))

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        if self.request.POST:
            context.update({
                'username': self.request.POST.get('username'),
                'password1': self.request.POST.get('password1'),
                'password2': self.request.POST.get('password2')
            })

        return context