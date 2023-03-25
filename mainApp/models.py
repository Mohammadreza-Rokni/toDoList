from django.db import models

# Create your models here.
class toDo(models.Model):
    title  = models.CharField(max_length=100, blank=False) # (blank=False) = field tip to be full
    Description = models.TextField(blank=True)  # (blank=True) = field can be empty
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self): # Create def __str__ that show title in admin
        return self.title

