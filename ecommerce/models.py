from django.db import models

from user.models import User


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField(default=15)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    bar_code = models.PositiveIntegerField(unique=True)

    def __str__(self) -> 'str':
        return self.title


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ticket = models.OneToOneField(to='Ticket', on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()

    def __str__(self) -> 'str':
        return f"<{self.ticket}>, {self.buyer}"
