from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #Relación 1 a muchos (one to many)
    #on_delete hace que "qué pasa si el usuario se borra"; en este caso se borra el Post también.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #no me acuerdo para qué servía esto lol
    def __str__(self):
        return self.title

    #Esto te redirecciona después de crear un Post. La función reverse te regresa el PATH como string.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})