from django.db import models
# Create your models here.


class Datepicker(models.Model):
    name = models.CharField(max_length=1000)
    dob = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Date Picker'
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)
