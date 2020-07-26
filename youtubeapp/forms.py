from django import forms
from .models import Vedio

class NewVedioForm(forms.ModelForm):
    class Meta:
        model = Vedio
        fields = ('Title', 'Discription','path')


class RegesterForm(forms.Form):
	username = forms.CharField(label='Username', max_length=20)
	password = forms.CharField(label='Password', max_length=20)
	email = forms.CharField(label='Email', max_length=20)

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=20)
	password = forms.CharField(label='Password', max_length=20)
		

class CommentsForm(forms.Form):
	text = forms.CharField(label='Comment', max_length=200)