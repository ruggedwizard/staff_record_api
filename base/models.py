from typing import Any
from django.db import models

# Create your models here.
class StaffRecords(models.Model):
    staff_id = models.IntegerField(unique=True,null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=1024, null=False, blank=False)
    confirmation_status = models.BooleanField(null=False,blank=False)
    staff_position = models.CharField(max_length=255, null=False, blank=False)
    staff_salary = models.FloatField(default=0.0)
    date_joined = models.DateTimeField(null=False, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} Profile Record"
    
 


