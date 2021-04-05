from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : "md-form-control", "placeholder" : "Please enter your name"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class' : "md-form-control", "placeholder" : "Please enter your email"}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : "md-form-control", "placeholder" : "Please enter a subject"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : "md-form-control", "placeholder" : "Your message", "rows" : 8, "cols" : 45}))

    def save(self):
        print("SAVVEAAAAAM")
