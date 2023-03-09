from django import forms

class UserRegistration(forms.Form):
    name = forms.CharField()
    def clean_name(self):
        clname = self.cleaned_data.get('name')
        if len(clname) < 4:
            raise forms.ValidationError('enter greater than or equal to 4 charectors!!!')
        return clname