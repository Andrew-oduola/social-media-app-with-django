from typing import Any
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image

import requests

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extentions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extentions:
            raise forms.ValidationError('The given URL does not' \
                                        'match valid image extensions.')
        return url
    
    def save(self, force_insert=False,
             force_update=False,
             commit: bool = True) -> Any:
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extention = image_url.rsplit('.', 1)[1].lower()
        image_name = f"{name}.{extention}"

        response = requests.get(image_url)
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)
        
        if commit:
            image.save()

        return image
    