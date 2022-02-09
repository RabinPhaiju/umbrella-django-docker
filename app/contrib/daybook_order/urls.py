from django.urls import path
from . import views


urlpatterns = [
    path('',views.Daybook_orderView.as_view(),name='daybook_order')
]

