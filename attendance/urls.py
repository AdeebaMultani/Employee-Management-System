from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_list, name='attendance_list'),

    path(
        'mark/',
        views.mark_attendance,
        name='mark_attendance'
    ),

    path(
        'edit/<int:pk>/',
        views.edit_attendance,
        name='edit_attendance'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_attendance,
        name='delete_attendance'
    ),
]
