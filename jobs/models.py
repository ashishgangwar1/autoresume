from django.db import models
from users.models import CustomUser

class JobDescription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    jd_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
