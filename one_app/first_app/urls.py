from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [ 
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),

    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),

]

 