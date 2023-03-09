from django import forms

class data(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        if len(valname) < 5:
            raise forms.ValidationError('enter more charectors in your name !!!')
        valemail = self.cleaned_data['email']
        if len(valemail) < 10: 
            raise forms.ValidationError("email should be more than or equal to 10 !!!")
