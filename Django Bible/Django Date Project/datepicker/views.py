from django.views.generic import CreateView
from .forms import DatepickerForm
from django.urls import reverse_lazy
from .models import Datepicker

# Create your views here.


class DatePickerView(CreateView):
    model = Datepicker
    form_class = DatepickerForm
    template_name = 'datepicker/datepicker.html'
    success_url = reverse_lazy('datepicker:dates')
