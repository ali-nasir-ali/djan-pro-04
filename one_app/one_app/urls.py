from django.contrib import admin
from django.urls import path , include
from first_app import views as first_app_views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('task/', include('first_app.urls')),
   #path('account/', include('users_app.urls')),
  
   path('', first_app_views.index, name='index'),
   path('contact/', first_app_views.contact, name='contact'),
   path('about/', first_app_views.about, name='about'),
   path('pricing/', first_app_views.pricing, name='pricing')
]
