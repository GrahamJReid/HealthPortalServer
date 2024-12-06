"""
URL configuration for grouprare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from healthportalapi.views import register_user, check_user,UserView,PatientIntakeFormView, get_patient_intake_form, DoctorPatientView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'patientintakeform', PatientIntakeFormView, 'patientintakeform')
router.register(r'doctorpatient', DoctorPatientView, 'doctorpatient')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
    path('api/getpatientintakeform/<int:patient_id>/', get_patient_intake_form, name='get_patient_intake_form'),
   

]
