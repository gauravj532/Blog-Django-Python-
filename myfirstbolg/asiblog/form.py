from django import forms
from models import Post
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class newPostForm(forms.ModelForm):
# 	class Meta:
# 		Model=Post
# 		fields=('title','body')
		
class loginForm(forms.ModelForm):
	class Meta:
		Model=User
		fields=('username','password')

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
	password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))

	class Meta:
		model = User
		fields =('username',)

		def save(self, commit=True):
			user = super(UserCreationForm,self).save(commit=False)
			user.email = self.cleaned_data['email']

			if commit:
				user.save()

			return user
# class Meta:
# 	Model=Post

    