from django import forms


class RegisterForm(forms.Form):
    username        = forms.CharField(label="Username", max_length=50)
    password1       = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
    password2       = forms.CharField(label="Password (again)", max_length=50, widget=forms.PasswordInput)
    first_name      = forms.CharField(label="First Name", max_length=50)
    last_name      = forms.CharField(label="Last Name", max_length=50)
    email           = forms.EmailField()

    def clean_password2(self):
        password1 = self.data['password1']
        password2 = self.data['password2']
        if password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.', code='password_mismatch')
        return password2
