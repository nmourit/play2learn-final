from django.forms import ModelForm, Textarea

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        widgets = {
            'review': Textarea(
                attrs={'cols': 80, 'rows': 5, 'autofocus': True}
            )
        }