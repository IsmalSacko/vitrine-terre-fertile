from django import forms
from django.forms import inlineformset_factory
from .models import HomePage, CarouselItem


class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = [
            'titre_principal',
            'description',
            'video',
            'video_poster',
            'hero_image',
            'featured_image_1',
            'featured_image_2',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


def get_carousel_formset(data=None, files=None, instance=None):
    CarouselFormSet = inlineformset_factory(
        HomePage,
        CarouselItem,
        fields=('ordre', 'image', 'titre', 'description', 'actif'),
        extra=1,
        can_delete=True,
    )
    return CarouselFormSet(data=data, files=files, instance=instance)
