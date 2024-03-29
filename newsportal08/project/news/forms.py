from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ['author', 'category', 'header', 'article_text', 'rating', ]

    def clean(self):
       cleaned_data = super().clean()
       name = cleaned_data.get("name")
       description = cleaned_data.get("description")

       #if vname == description:
       #    raise ValidationError(
       #        "Описание не должно быть идентично названию."
       #    )

       return cleaned_data