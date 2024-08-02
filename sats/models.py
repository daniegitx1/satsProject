from django.db import models


class SatsModel(models.Model):
    amount = models.IntegerField(default=0,)

    def __str__(self):
        return str(self.amount)
