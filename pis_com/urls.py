from django.urls import path, include,re_path


from pis_com.views.com.home import HomePageView
from pis_com.views.com.users.login import LoginView
from pis_com.views.com.users.logout import LogoutView
from pis_com.views.com.customer import (
    CreateCustomer, CustomerTemplateView, CustomerUpdateView)
from pis_com.views.com.create_feedback import CreateFeedBack
from pis_com.views.com.users.register import RegisterView
from pis_com.views.com.reports.reports import ReportsView

urlpatterns = [
    re_path(r'^$', HomePageView.as_view(), name='index'),
    re_path(r'^reports/$', ReportsView.as_view(), name='reports'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),

    #path('api/', include('pis_com.api_urls', namespace='com_api')),
    re_path(r'^api/',CreateCustomer.as_view(),name='create_customer'),

    re_path(r'^customer/create/$', CustomerTemplateView.as_view(), name='customers'),

    re_path(r'^customers/$', CustomerUpdateView.as_view(), name='update_customer'),
    re_path(r'^customer/(?P<pk>\d+)/update$', RegisterView.as_view(), name='register'),
    re_path(r'^register/$', CreateFeedBack.as_view(), name='create_feedback'),
]
