from django.urls import path
from datepicker import views

app_name = 'datepicker'

urlpatterns = [
    path('dates/', views.DatePickerView.as_view(), name='dates'),
]
