from django import forms


class NameForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20)
    last_name = forms.CharField(label='Last name', max_length=20)
    user_email = forms.EmailField(label='email', max_length=20)
