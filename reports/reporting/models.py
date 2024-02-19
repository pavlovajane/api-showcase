from django.db import models

# Create your models here.
class Report(models.Model):
   
    title = models.CharField(max_length = 5)
    date = models.DateField()
    body = models.TextField()

    class Meta:
        verbose_name_plural = "Reports"