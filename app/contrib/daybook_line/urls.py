from django.urls import path
from . import views


urlpatterns = [
    path('',views.Daybook_lineView.as_view(),name='daybook_line')
]

