from django.db import models
#Para importar el usuario que te genera Django que hemos estado usando en todo el proyecto!
from django.contrib.auth.models import User
#Pillow permite redimensionar imágenes
from PIL import Image

class Profile(models.Model):
    #relación uno a uno (1:1)
    #on_delete significa que se borra el perfil si se borra el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #def save(self):
    def save(self, *args, **kwargs):
        #esto de abajo da error en mysql. Gracias stackoverflow
        #super().save()
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)