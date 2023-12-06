from django.db import models
from django.contrib.auth.models import User

class Historial(models.Model):
    code = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.date}"





