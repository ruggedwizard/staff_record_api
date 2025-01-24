from django.db import models

# Create your models here.
class StaffRecords(models.Model):
    staff_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=255, null=False, blank=False)

    