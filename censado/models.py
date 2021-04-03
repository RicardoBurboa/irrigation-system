from django.db import models


class Censado(models.Model):
    temperatura_LM35 = models.FloatField(max_length=10)
    temperatura_DS18B20 = models.FloatField(max_length=10)
    humedad_HL69 = models.FloatField(max_length=10)
    status_riego = models.IntegerField()
    anomalia = models.IntegerField()
    hora = models.IntegerField()
    
    #def __str__(self):
    #    return self.temperatura_LM35
