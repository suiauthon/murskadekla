from django import forms

class PlantATreeForm(forms.Form):
    key = forms.CharField(
        max_length=8,
        widget=forms.TextInput(attrs={'class': "md-plant-a-tree-key-input"}))

    def clean_key(self):
        pass
