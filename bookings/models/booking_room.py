from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError, FieldError
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
    user = models.ForeignKey(
        get_user_model(),
        related_name="booked_room",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "bookings"

    def __str__(self):
        return f"{self.room.number} - from {self.start_date} to {self.end_date}"

    # def clean(self):
    #     if self.start_date <= date.today():
    #         raise ValidationError("start_date must be greater than the current date.")
    #     if self.start_date > self.end_date:
    #         raise ValidationError("start_date can't be greater than end_date!")
    #     if self.end_date - self.start_date > timedelta(3):
    #         raise ValidationError("You can't book a room for more than 3 days!")
    #     if self.start_date - date.today() > timedelta(30):
    #         raise ValidationError("You can't book a room more than 30 days in advance!")

    # def save(self, *args, **kwargs):
    #
    #     start = Booking.objects.filter(start_date=self.start_date)
    #     end = Booking.objects.filter(end_date=self.end_date)
    #
    #     if start:
    #         raise ValidationError("The start_date chosen is already booked!")
    #
    #     if end:
    #         raise ValidationError("The end_date chosen is already booked!")
    #
    #     super(Booking, self).save(*args, **kwargs)



        # if self.start_date and self.end_date:
        #     try:
        #         current_date = self.start_date > date.today()
        #         date_gt_3 = self.end_date - self.start_date > timedelta(3)
        #         # start_lt_end = self.start_date > self.end_date
        #
        #         super(Booking, self).save(*args, **kwargs)
        #     except FieldError:
        #         raise ValidationError("review your paylod!")


