from django.db import models

from rooms.models import Room


class Booking(models.Model):
    start_date = models.DateField(verbose_name="Date d'entrée")
    end_date = models.DateField(verbose_name="Date de sortie")
    room = models.ForeignKey(
        Room,
        related_name="booked_room",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "bookings"

    def __str__(self):
        return f"{self.room.number} - from {self.start_date} to {self.end_date}"


