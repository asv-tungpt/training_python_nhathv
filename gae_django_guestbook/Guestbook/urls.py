__author__ = 'NhatHV'

from django.conf.urls import patterns
from guestbook.views import main_page, sign_post

urlpatterns = patterns('',
    (r'^sign/$', sign_post),
    (r'^$', main_page),
)