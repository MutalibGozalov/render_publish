from django.db import models
from summaryapp.models import ServiceModel, BarberModel

class AssingmentModel(models.Model):
    employee = models.ForeignKey(BarberModel, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tip = models.DecimalField(max_digits = 4, decimal_places = 2)

    class Meta:
        db_table = 'assignment'
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return "Assignement"