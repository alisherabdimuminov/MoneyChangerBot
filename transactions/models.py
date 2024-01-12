from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=50)
    validator = models.CharField(max_length=50)
    example = models.CharField(max_length=50)
    allowed_cards = models.ManyToManyField("self", related_name="cards_for_payment", null=True, blank=True)

    def __str__(self):
        return self.name
