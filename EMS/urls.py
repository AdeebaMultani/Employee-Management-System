
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Authentication
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Employees
    path('employees/', include('employees.urls')),

    # Departments
    path('departments/', include('departments.urls')),

    # Attendance
    path('attendance/', include('attendance.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
