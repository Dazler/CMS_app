from django import forms

from .models import Aircraft,NewsFeed

class AircraftForm(forms.ModelForm):

    class Meta:
        model = Aircraft
        fields = ('__all__')


"""class NewsFeedForm(forms.ModelForm):

    class Meta:
        model = NewsFeed
        fields = ('hl','ct')"""