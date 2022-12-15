from django.db import models

class ServiceModel(models.Model):
    name = models.CharField(max_length=30, blank = False, null=False)
    time = models.DurationField(blank = True, null = True)
    prize = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        db_table = 'service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.name