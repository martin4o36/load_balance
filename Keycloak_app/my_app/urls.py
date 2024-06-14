from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-person/', views.add_person, name='add_person'),
    path('remove-person/', views.remove_person, name='remove_person'),
    path('add-event/', views.add_event, name='add_event'),
    path('remove-event/', views.remove_event, name='remove_event'),
    path('get-all-events/', views.get_all_events, name='get_all_events'),
]