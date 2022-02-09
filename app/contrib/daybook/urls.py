from django.urls import path
from . import views


urlpatterns = [
    path('',views.DaybookView.as_view(),name='daybook')
]

