from django.db import models

class Commande(models.Model):

    name = models.CharField("Nom de l'article", max_length=50)
    title = models.CharField("Titre", max_length=254)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self):
        return self.name
