from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to='images')

    class Meta:
        verbose_name_plural = 'User_profile'
    
    def __str__(self) -> str:
        return f'{self.user}'
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = User_profile(user=instance)
        user_profile.save()
