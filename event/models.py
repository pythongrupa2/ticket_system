from django.db import models
from django import forms
from phone_field import PhoneField


class Event(models.Model):
    name_event = models.CharField(max_length=150, blank=False, null=False, verbose_name=("Title of Event"))
    performer = models.CharField(max_length=100, blank=False, null=False, verbose_name=("Name of Showmans"))
    date_event = models.DateField(blank=False, null=False)
    hour_event = models.TimeField(blank=False, null=False)
    price_ticket = models.DecimalField(blank=False, null=False)
    event_type = models.CharField(max_length=15, blank=True, null=False, verbose_name=("Type of Event"))

    def __str__(self):
        return self.name_event, self.performer, self.date_event

TICKET_TYPE_CHOICES = (
    ("1", "Standard"),
    ("2", "VIP"),
)

# class TicketType(forms.Form):
#     ticket_type = forms.CharField(choices = TICKET_TYPE_CHOICES)

class Ticket(models.Model):
    ticket_type = forms.CharField(choices = TICKET_TYPE_CHOICES)
    date_reservation = models.DateField(blank=True, null=True)
    date_purchase = models.DateField(blank=False, null=False)
    date_ticket_return = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ticket_type, self.date_reservation, self.date_purchase, self.date_ticket_return

class Payment(models.Model):
    payment_type = models.CharField(max_length=50, blank=False, null=False, verbose_name=("Type of Payment"))
    date_payment = models.DateField(blank=False, null=False, verbose_name=("Date of Payment"))
    date_payment_return = models.DateField(blank=True, null=True)
    payment_amount = models.DecimalField(blank=False, null=False)

    def __str__(self):
        return self.payment_type, self.date_payment, self.date_payment_return, self.payment_amount

class User(models.Model):
    user_login = models.CharField(max_length=50, blank=False, null=False, verbose_name=("User Login"))
    user_email = models.CharField(max_length=100, blank=False, null=False, verbose_name=("User Email"))
    user_phone = PhoneField(blank=True, help_text="Contact phone number")

    def __str__(self):
        return self.user_login, self.user_email, self.user_phone

class Operator(models.Model):
    user_name = models.CharField(max_length=50, blank=False, null=False, verbose_name=("User Name"))
    user_surname = models.CharField(max_length=50, blank=False, null=False, verbose_name=("User Surname"))

    def __str__(self):
        return self.user_name, self.user_surname