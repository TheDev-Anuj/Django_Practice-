from django import forms

class data(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput)
    rpasswd = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        valpasswd = self.cleaned_data['passwd']
        print('passwd is: ', cleaned_data['passwd'])
        valrpasswd = self.cleaned_data['rpasswd']
        print('rpasswd is: ', cleaned_data['rpasswd'])
        if valpasswd != valrpasswd:
            raise forms.ValidationError('password do not match!!!')
        valname = cleaned_data['name']
        if len(valname) < 5:
            raise forms.ValidationError('enter more charectors in your name !!!')
        valemail = cleaned_data['email']
        if len(valemail) < 10: 
            raise forms.ValidationError("email should be more than or equal to 10 !!!")

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = cleaned_data['name']
    #     if len(valname) < 5:
    #         raise forms.ValidationError('enter more charectors in your name !!!')
    #     valemail = cleaned_data['email']
    #     if len(valemail) < 10: 
    #         raise forms.ValidationError("email should be more than or equal to 10 !!!")
 