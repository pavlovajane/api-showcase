from django.db import models

# Create your models here.
class Report(models.Model):
   
    title = models.CharField(max_length = 50, null=False, blank=True)
    date = models.DateField(null=True, blank=True)
    body = models.TextField(null=False, blank=True)

    class Meta:
        verbose_name_plural = "Reports"