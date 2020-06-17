from django.db import models

class CustomBaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    notes = models.CharField(null = True, blank = True, max_length = 2048)
    # This set the class as abstract class and does not create a 1 to 1 relation when extending the class
    class Meta:
        abstract = True