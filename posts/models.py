import misaka
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from groups.models import Group

User = get_user_model()


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-create_at']
        unique_together = ['user', 'group']
