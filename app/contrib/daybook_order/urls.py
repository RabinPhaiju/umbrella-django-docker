from django.urls import path
from . import views


urlpatterns = [
    path('',views.Daybook_typeView.as_view(),name='daybook_type')
]

