from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class LoginForm(forms.Form):
	username = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				"placeholder":"username",
			}
			)
		)
	password = forms.CharField(
		label='',
		widget=forms.PasswordInput(
			attrs={
				"placeholder":"password",
			}
			)
		)
	# def clean_username(self):
	# 	username=self.cleaned_data.get('username')
	# 	if not len(username):
	# 		raise forms.ValidationError('Username cannot be empty')
	# 	qs = User.objects.filter(username=username)
	# 	if  not qs.exists():
	# 		raise forms.ValidationError("Username doesn't exist")
	# 	return username
	
	def clean(self):
		data=self.cleaned_data
		username=self.cleaned_data.get('username')
		password=self.cleaned_data.get('password')
		qs = User.objects.filter(password=password)
		if qs.exists() and qs.count()==1:
			print('valid password, checking for username')
			qs2 = User.objects.filter(username=username)
			if qs2.exists() and qs2.count()==1:
				raise forms.ValidationError('Invalid username')
			
		else:
			raise forms.ValidationError('Invalid Password')
			
			print(self.cleaned_data)
			
		return data

	# def clean_password(self):
	# 	password=self.cleaned_data.get('password')
	# 	if not len(password):
	# 		raise forms.ValidationError('Password cannot be empty')
	# 	qs = User.objects.filter(password=password)
	# 	print('queryset',qs)
	# 	print('entered password is ',password)
	# 	if not qs.exists():
	# 		raise forms.ValidationError('Invalid Password')
	# 		print(qs)
	# 	return password

class RegisterForm(forms.Form):
	fullname = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				"placeholder":"Full name",
			}
			)
		)
	username = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				"placeholder":"Username",
			}
			)
		)
	password = forms.CharField(
		label='',
		widget=forms.PasswordInput(
			attrs={
				"placeholder":"Password",
			}
			)
		)
	password2 = forms.CharField(
		label='',
		widget=forms.PasswordInput(
			attrs={
				"placeholder":"Confirm password",
			}
			)
		)
	email = forms.EmailField(
		label='',
		widget=forms.TextInput(
			attrs={
				"placeholder":"E-mail",
				#"class":"form-control"
			}
			)
		) 

	def clean_username(self):
		username=self.cleaned_data.get('username')
		if not len(username):
			raise forms.ValidationError('Username cannot be empty')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError('Username already exists.')
		return username

	def clean_email(self):
		email=self.cleaned_data.get('email')
		if '@' not in email or '.' not in email:
			raise forms.ValidationError("Invalid email")
		return email

	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError('Both password should be same')
		return data