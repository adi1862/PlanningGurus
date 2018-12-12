from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model 
#from appname.filename import classname
from pg.forms import LoginForm,RegisterForm
# Create your views here.

def home_view(request,*args,**kwargs): 
	print('in home view')
	print(kwargs)
	form=LoginForm(request.POST or None)
	context={
		'title':'Planning Gurus',
		'form': form
	}
	if form.is_valid():
		if request.user.is_authenticated:
			print('Valid user.Redirecting to the homepage')
			return redirect('../') #redirect to the home page
		else:
			print('not a  valid user')
		context={
			'form':LoginForm()
		}
	return render(request, "home.html", context)

temp_user = get_user_model()

def login_page(request):
	form = LoginForm(request.POST or None)
	context={"form":form}
	if form.is_valid():
		print('Entered:',form.cleaned_data)
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		if user is not None:
		# if request.user.is_authenticated:
			login(request,user)
			print('Valid user.Redirecting to the homepage',user)
			print(form.cleaned_data)

			# temp_user = get_user_model()
			# qs = temp_user.objects.filter(username=username)
			# print('Detail found:',qs.objects.all())

			# context['username']=username
			# logout(request)
			return redirect('../') #redirect to the home page
			# return render(request, "home.html", {})
		else:
			print('***NOT**** a valid user')
			# raise forms.ValidationError('Incorrect Username or password')
			# context={'form':LoginForm()}
	return render(request, "login.html",context)

User = get_user_model()
def register_view(request):
	form=RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		new_user = User.objects.create_user(username,email,password)
		new_user.save()
		print('Registration successfull. Redirecting to homepage')
		context={'form':RegisterForm()}
		return redirect('../')
	else:
		context={'form':form}
	return render(request,'register.html',context)

def logout_view(request,*args,**kwargs):
	logout(request)
	return redirect('../')

def about_view(request,*args,**kwargs):
	return render(request,"about.html",{})

def coming_soon(request,*args,**kwargs):
	return render(request,"coming_soon.html",{})

def contact_view(request,*args,**kwargs):
	return render(request,"contact.html",{})