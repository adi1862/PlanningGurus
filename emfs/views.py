from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import Emf

class EmfListView(ListView):
	# queryset = Emf.objects.all()  we're using 'get_queryset()' instead of this statement
	template_name = 'emfs/emflist.html' 

	def get_context_data(self,*args,**kwargs):
		context = super(EmfListView,self).get_context_data(*args,**kwargs)
		print(context)
		return context
	def get_queryset(self,*args,**kwargs): #overriding the 'get_queryset()' method
		request= self.request
		return Emf.objects.all()

#for SEARCH, we can use 'queryset = Emf.object.filter()'

class EmfDetailView(DetailView):
	# queryset = Emf.objects.all() 'we're using get_object() instead of this statement
	template_name = 'emfs/emfdetail.html'

	def get_context_data(self,*args,**kwargs):
		context = super(EmfDetailView,self).get_context_data(*args,**kwargs)
		print(context)
		return context	

	def get_object(self,*args,**kwargs): #overriding the 'get_object()' method', with help of our 'get_by_id()'
		request 	= self.request
		pk 			= self.kwargs.get('pk')
		instance 	= Emf.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Emf doesn't exist")
		return instance