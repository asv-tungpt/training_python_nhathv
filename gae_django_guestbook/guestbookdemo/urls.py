__author__ = 'NhatHV'

from django.conf.urls import patterns, url

from guestbookdemo import views
from guestbookdemo.utils import SendEmail

urlpatterns = patterns('',
    url(r'^$', views.MainPageView.as_view(), name='mainpage'),
    url(r'^sign_guestbook/$', views.SignGuestbook.as_view(), name='sign_guestbook'),
    url(r'^switch_guestbook/$', views.SwitchGuestbook.as_view(), name='switch_guestbook'),
    url(r'^send_email/$', SendEmail.as_view()),
    url(r'^delete/$', views.MainPageView.as_view(), name='mainpage-delete-message'),
    url(r'^edit/$', views.EditGreeting.as_view(), name='edit-message'),
    url(r'^save_greeting/$', views.EditGreeting.as_view(), name='save-message'),
)