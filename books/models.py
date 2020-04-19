from django.db import models


# Create your models here.
class Books(models.Model):
    Name = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=100)
    No_of_Copies = models.PositiveIntegerField(default=0)
    Publisher_Name = models.CharField(max_length=255, null=True, blank=True)
    Publish_Date = models.DateField(null=True, blank=True)
    Create_On = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.Name
