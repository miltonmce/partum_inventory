from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
from django.contrib.auth import logout as auth_logout
from django.urls import reverse


class LogoutView(RedirectView):

    def dispatch(self, request, *args, **kwargs):
        auth_logout(self.request)
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('login'))