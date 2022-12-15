from django.db import models

class BarberModel(models.Model):
    name = models.CharField(max_length=30, blank = False, null=False) 
    joined = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'barber'
        verbose_name = 'Barber'
        verbose_name_plural = 'Barbers'

    def __str__(self):
        return self.name