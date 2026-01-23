from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to_home(instance, filename):
    return f'home/{filename}'


class HomePage(models.Model):
    """Singleton model pour le contenu éditable de la page d'accueil."""
    titre_principal = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to=upload_to_home, blank=True, null=True, help_text=_('Fichier vidéo mp4'))
    video_poster = models.ImageField(upload_to=upload_to_home, blank=True, null=True)

    # images secondaires (ex: home_terre_fertile.png) — on stocke les chemins modifiables
    hero_image = models.ImageField(upload_to=upload_to_home, blank=True, null=True)
    featured_image_1 = models.ImageField(upload_to=upload_to_home, blank=True, null=True)
    featured_image_2 = models.ImageField(upload_to=upload_to_home, blank=True, null=True)

    # Configuration utile
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Page d\'accueil')
        verbose_name_plural = _('Pages d\'accueil')

    def __str__(self):
        return "Contenu page d'accueil"


class CarouselItem(models.Model):
    """Items du carousel de la home page."""
    # lien optionnel vers HomePage pour l'inline admin
    homepage = models.ForeignKey(HomePage, related_name='carousel_items', on_delete=models.CASCADE, null=True, blank=True)
    ordre = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=upload_to_home)
    titre = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ['ordre']
        verbose_name = _('Élément du carousel')
        verbose_name_plural = _('Éléments du carousel')

    def __str__(self):
        return self.titre or f"Carousel #{self.pk}"
