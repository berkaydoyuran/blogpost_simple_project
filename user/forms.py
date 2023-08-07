from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kimsin")
    password = forms.CharField(label = "Parolan",widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50 , label= 'Kimsin')
    password = forms.CharField(max_length=50 , label= 'Parolan', widget= forms.PasswordInput)
    confirm = forms.CharField(max_length=50 , label= 'Bi Daha', widget= forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError('aynisini gir amk')
        
        values = {
            'username' : username,
            'password' : password
        }

        return values