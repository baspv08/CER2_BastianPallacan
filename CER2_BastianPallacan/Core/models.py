from django.db import models

class residencia(models.Model):
    numero_res = models.CharField(max_length=30)
    dueño_res = models.CharField(max_length=30)
    fono_dueño = models.CharField(max_length=30)
    email_dueño = models.CharField(max_length=30)

    def __str__(self):
        return self.numero_res +' - '+self.dueño_res

correspondencia_estado =[
    (1,'Entregado'),
    (2,'En envio'),
    (3,'No entregado')
]

class correspondencia(models.Model):
    fecha_recepcion =models.CharField(max_length=30)
    conserje_remitente =models.CharField(max_length=30)
    destinatario =models.CharField(max_length=30)
    estado =models.IntegerField(
        null=False ,blank=False,
        choices=correspondencia_estado,
        default=1
    ) 
    
    def __str__(self):
        return self.destinatario
