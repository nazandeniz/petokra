
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Pet(models.Model):
    SPECIES_CHOICES = [
        ("cat", _("Cat")),
        ("dog", _("Dog")),
        ("bird", _("Bird")),
        ("other", _("Other")),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pets",
    )

    name = models.CharField(
        _("Name"),
        max_length=100,
    )

    species = models.CharField(
        _("Species"),
        max_length=20,
        choices=SPECIES_CHOICES,
    )

    breed = models.CharField(
        _("Breed"),
        max_length=100,
        blank=True,
    )

    birth_date = models.DateField(
        _("Birth date"),
        null=True,
        blank=True,
    )

    photo_url = models.URLField(
        _("Photo URL"),
        blank=True,
    )

    notes = models.TextField(
        _("Notes"),
        blank=True,
    )

    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name} ({self.get_species_display()})"

    class Meta:
        verbose_name = _("Pet")
        verbose_name_plural = _("Pets")
        ordering = ["-created_at"]
