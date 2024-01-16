from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=500, blank=False)


class Testemunho(models.Model):
    EXPLICADORE = "Explicadore"
    EXPLICADOR = "Explicador"
    EXPLICADORA = "Explicadora"
    EXPLICANDE = "Explicande"
    EXPLICANDO = "Explicando"
    EXPLICANDA = "Explicanda"
    OCCUPATIONS = [
        (EXPLICADORE, EXPLICADORE),
        (EXPLICADOR, EXPLICADOR),
        (EXPLICADORA, EXPLICADORA),
        (EXPLICANDE, EXPLICANDE),
        (EXPLICANDO, EXPLICANDO),
        (EXPLICANDA, EXPLICANDA),
    ]
    text = models.TextField(blank=False)
    year = models.CharField(max_length=5, blank=False)
    occupation = models.CharField(
        max_length=11, choices=OCCUPATIONS, default=EXPLICADORE
    )
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            "text": self.text,
            "year": self.year,
            "occupation": self.occupation,
            "username": self.user.name if self.user else None,
        }
