from django.views.generic import TemplateView


class dashboard(TemplateView):
    template_name = 'expense/dashboard.html'
