from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Employees
    path('employees/', include('employees.urls')),

]