from django import forms

from .models import Artist

class ArtistForm(forms.ModelForm):
  
    class Meta:
        model = Artist
        fields = ("name",)

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({
            "class":"form-control",
        })