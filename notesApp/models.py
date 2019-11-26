from django.db import models
from datetime import datetime
# Create your models here.
class notes(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank = True)

    def __str__(self):
        return self.text