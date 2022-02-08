from django.db import models


class Room(models.Model):
    number = models.IntegerField(verbose_name="Numero", unique=True)
    size = models.FloatField(verbose_name="Taille")
    nb_bed = models.IntegerField(verbose_name="Nombre de lit")
    type_of_bed = models.CharField(verbose_name="Type de lit", max_length=250)
    frigo_bar = models.BooleanField(verbose_name="Frigo Bar", default=False)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = "Rooms"

    def __str__(self):
        return f"{self.number} {self.type_of_bed}"

