from django.db import models
from user.models import User

class reportLog(models.Model):
    reportDate = models.DateTimeField(auto_now_add=True)
    reportData = models.CharField(max_length=100)
    reportUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.reportData

# Create your models here.
