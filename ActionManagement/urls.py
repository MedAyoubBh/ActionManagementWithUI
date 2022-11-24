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
    path('static/admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('static/Consult',views.consult),
    path('static/CreatePA',views.createPA,name='createPA'), 
    path('static/PAE',views.PAE,name='PAE'),
    path('static/CreateProblem',views.createProblem,name='createProblem'), 
    path('static/CreateAction',views.createAction,name='createAction'),
    path('static/CreateAxe',views.createAxe,name='createAxe'),
    path('static/AddPage',views.addPage,name='addPage'), 
    path('static/UpdateP',views.updateP,name='updateP'), 
    path('static/UpdateD',views.updateD,name='updateD'),  
    path('static/UpdateC',views.updateC,name='updateC'),  
    path('static/UpdateA',views.updateA,name='updateA'),  
    path('static/Login',views.login,name='login'), 
    path('static/Logout',views.logout,name='logout'), 
    path('static/rev',views.rev,name='rev'),
    path('static/ModificateParticipants',views.modificateParticipants,name='modificateParticipants'),
    path('static/ModificateAxe',views.modificateAxe,name='modificateAxe'),
    path('static/ModificateProblem',views.modificateProblem,name='modificateProblem'),
    path('static/ModificateAction',views.modificateAction,name='modificateAction'),
    path('static/CreateUser',views.createUser,name='createUser'),
    path('static/DeleteUser',views.deleteUser,name='deleteUser'),
    path('static/ConsultUsers',views.consultUsers,name='consultUsers'),
    path('static/ModificateUser',views.modificateUser,name='modificateUser'),
    path('static/ConsultSecters',views.consultSecters,name='consultSecters'),
    path('static/ModificateSecter',views.modificateSecter,name='modificateSecter'),
    path('static/DeleteSecter',views.deleteSecter,name='deleteSecter'),
    path('static/CreateSecter',views.createSecter,name='createSecter'),
    path('static/Dashboard',views.dashboard,name='dashboard'),
    path('static/DashboardForm',views.dashboardForm,name='dashboardForm'),
    path('static/ModificateCheckers',views.modificateCheckers,name='modificateCheckers'),
    path('static/ModificateActors',views.modificateActors,name='modificateActors'),
    path('static/ConsultAllMyActions',views.consultAllMyActions,name='consultAllMyActions'),
    path('static/ConsultAllMyPA',views.consultAllMyPA,name='consultAllMyPA'),
    path('static/Historic',views.historic,name='historic'),
    path('static/PrintPA',views.printPA,name='printPA'),
    re_path (r'^.*$', RedirectView.as_view (url='/', permanent=False), name='home')
]