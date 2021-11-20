from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    
    task_number = models.IntegerField(blank=False, null=False)
    task_name = models.CharField(max_length=200)
    task_des = models.CharField(max_length=200)
    due_date = models.DateTimeField(blank=False, null=False)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_number)

