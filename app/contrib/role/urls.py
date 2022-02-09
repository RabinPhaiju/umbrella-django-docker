from django.urls import path
from . import views


urlpatterns = [
    path('',views.RoleView.as_view(),name='role')
]

