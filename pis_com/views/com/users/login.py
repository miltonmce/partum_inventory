from django.views.generic import FormView
from django.contrib.auth import forms as auth_forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login
from pis_com.models import AdminConfiguration


class LoginView(FormView):
    template_name = 'login.html'
    form_class = auth_forms.AuthenticationForm

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            if (
                    self.request.user.retailer_user.role_type ==
                    self.request.user.retailer_user.ROLE_TYPE_LEDGER_VIEW
            ):
                return HttpResponseRedirect(
                    reverse('customer_ledger_list'))

            return HttpResponseRedirect(reverse('index'))

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)

        return HttpResponseRedirect(reverse('index'))

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        try:
            admin_config = AdminConfiguration.objects.get(id=1)
            context.update({
                'config': admin_config
            })
        except AdminConfiguration.DoesNotExist:
            pass
        return context