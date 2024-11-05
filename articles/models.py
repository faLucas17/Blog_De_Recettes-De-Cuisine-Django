from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=150)
    resume = models.CharField(max_length=2000)
    contenu = models.TextField(blank=True)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Changez ici
    date_pub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True) # Nouveau champ image
    
    def __str__(self):
        return f"{self.titre}"