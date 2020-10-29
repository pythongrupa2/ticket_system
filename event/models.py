from django.db import models


class Event(models.Model):
    name_event = models.CharField(max_length=150, blank=False, null=False, verbose_name=("Title of Event"))
    performer = models.CharField(max_length=100, blank=False, null=False, verbose_name=("Name of Showmans"))
    date_event = models.DateField(blank=False, null=False)
    hour_event = models.TimeField(blank=False, null=False)
    price_ticket = models.FloatField(blank=False, null=False)
    event_type = models.CharField(max_length=15, blank=True, null=False, verbose_name=("Type of Event"))

    def __str__(self):
        return self.name_event, self.performer, self.date_event
