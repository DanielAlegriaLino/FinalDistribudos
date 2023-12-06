from django.db import models

class Historial(models.Model):
    code = models.TextField()
    date = models.DateField()
    user = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user} - {self.date}"





