from django import forms


class NameForm(forms.Form):
    first_name = forms.CharField(label='First name',
                                 max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': 'input your name'}))
    last_name = forms.CharField(label='Last name',
                                max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'input your last name'}))
    user_email = forms.EmailField(label='email',
                                  max_length=20,
                                  widget=forms.TextInput(attrs={'placeholder': 'input your e-mail'}))

