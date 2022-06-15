from django.db import models
from matplotlib.pyplot import title

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    
    def _str_ (self):
        return self.title
    