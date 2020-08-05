from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.urls import reverse
from pis_com.forms.customer.feedback import FeedBackForm


class CreateFeedBack(FormView):
    form_class = FeedBackForm
    template_name = 'create_feedback.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(
            CreateFeedBack, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('create_feedback'))

    def form_invalid(self, form):
        return super(CreateFeedBack, self).form_invalid(form)