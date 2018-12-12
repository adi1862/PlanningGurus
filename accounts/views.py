from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView 

from django import forms
from .forms import LoginForm, RegisterForm

# Create your views here.

class LoginView(FormView):
	form_class = LoginForm
	template_name ='login.html'
	success_url = '../'

	def form_valid(self,form):
		request = self.request
		next_ = request.GET.get('next')
		next_post = request.POST.get('next')
		redirect_path = next_ or next_post or None

		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		# exp are
		print('data',form.cleaned_data)
		# 

		user = authenticate(request,usename=email, password=password)
		print(user)
		if user is not None:
			login(request,user)
			print('user logged in')
			if is_safe_url(redirect_path,request.get_host()):
				print('redirect path', redirect_path)
				return redirect(redirect_path)
			else:
				return redirect("../")
		print('invalid credentials')
		return super(LoginView,self).form_invalid(form)

def login_page(request):
	form = LoginForm(request.POST or None)
	context={'form':form}
	# temp area
	# end of temp area
	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(request,username = email, password = password)
		if user is not None:
			login(request,user)
			print('login SUCCESSFULL')
			return redirect('../')
		else:
			context['generate'] = True
			# raise forms.ValidationError('Invalid credentials. Please sign up.')
	# print('<<<invalid credentials>>>')
	return render(request,'login.html',context)

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'register.html'
	success_url = '../login'

# User = get_user_model()
# def register_page(request):
# 	form = RegisterForm(request.POST or None)
# 	context = {
# 		'form': form
# 	}
# 	if form.is_valid():
# 		form.save()
# 		return redirect('../login')
# 	print('Invalid form')
# 	return render(request,'register.html',context)