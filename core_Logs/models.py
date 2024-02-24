from django.db import models
from core_Profile.models import User_profile

class Log(models.Model):
    profile = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='logs', blank=True, null=True)
    is_correct =models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.profile} || {self.is_correct}"