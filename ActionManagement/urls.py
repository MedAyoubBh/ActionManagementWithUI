"""ActionManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('Consult',views.consult),
    path('CreatePA',views.createPA,name='createPA'), 
    path('PAE',views.PAE,name='PAE'),
    path('CreateProblem',views.createProblem,name='createProblem'), 
    path('CreateAction',views.createAction,name='createAction'),
    path('CreateAxe',views.createAxe,name='createAxe'),
    path('AddPage',views.addPage,name='addPage'), 
    path('UpdateP',views.updateP,name='updateP'), 
    path('UpdateD',views.updateD,name='updateD'),  
    path('UpdateC',views.updateC,name='updateC'),  
    path('UpdateA',views.updateA,name='updateA'),  
    path('Login',views.login,name='login'), 
    path('Logout',views.logout,name='logout'), 
    path('rev',views.rev,name='rev'),
    path('ModificateParticipants',views.modificateParticipants,name='modificateParticipants'),
    path('ModificateAxe',views.modificateAxe,name='modificateAxe'),
    path('ModificateProblem',views.modificateProblem,name='modificateProblem'),
    path('ModificateAction',views.modificateAction,name='modificateAction'),
    path('CreateUser',views.createUser,name='createUser'),
    path('DeleteUser',views.deleteUser,name='deleteUser'),
    path('ConsultUsers',views.consultUsers,name='consultUsers'),
    path('ModificateUser',views.modificateUser,name='modificateUser'),
    path('ConsultSecters',views.consultSecters,name='consultSecters'),
    path('ModificateSecter',views.modificateSecter,name='modificateSecter'),
    path('DeleteSecter',views.deleteSecter,name='deleteSecter'),
    path('CreateSecter',views.createSecter,name='createSecter'),
    path('Dashboard',views.dashboard,name='dashboard'),
    path('DashboardForm',views.dashboardForm,name='dashboardForm'),
    path('ModificateCheckers',views.modificateCheckers,name='modificateCheckers'),
    path('ModificateActors',views.modificateActors,name='modificateActors'),
    path('ConsultAllMyActions',views.consultAllMyActions,name='consultAllMyActions'),
    path('ConsultAllMyPA',views.consultAllMyPA,name='consultAllMyPA'),
    path('Historic',views.historic,name='historic'),
    re_path (r'^.*$', RedirectView.as_view (url='/', permanent=False), name='home')
]