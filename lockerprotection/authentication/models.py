from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    fileUpload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.fileName