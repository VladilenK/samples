# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from django.urls import path

from . import views

urlpatterns = [
    # /
    path('', views.home, name='home'),
    # TEMPORARY
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),
    path('calendar', views.calendar, name='calendar'),
    path('sharepoint', views.sharepoint, name='sharepoint'),
    path('site/<str:id>', views.site_details, name='site_details'),
    path('teams', views.msteams, name='teams'),
]
