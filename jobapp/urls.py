from django.urls import path
from.views import *

urlpatterns=[

    path('index',index),
    path('log',login),
    path('regis',register),
    # path('navbar',navbar),
    # path('footer',footer),
    path('profile',profile),
    path('addjob/<int:id>',jobview),
    path('jobdisplay',jobdisplay),
    path('delete/<int:id>',delete),
    path('edit/<int:id>',edit),
    path('userreg',usereg.as_view(),name='userreg'),
    path('userlog',userlog.as_view(),name='userlog'),
    # path('userreg/', uregister),
    # path('userlogin/', ulogin),


]