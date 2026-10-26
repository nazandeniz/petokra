
from django.conf import settings
from django.db import models


class Pet(models.Model):
    SPECIES_CHOICES = [
        ("cat", "Kedi"),
        ("dog", "Köpek"),
        ("bird", "Kuş"),
        ("other", "Diğer"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pets",
    )
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_species_display()})"
