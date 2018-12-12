from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from emfs.models import Emf
# Create your views here.

possibles_events = ['birthday','Birthday','bday',"b'day",'wedding','Wedding','Anniversary','anniversary',
					'reception','Reception','special','Special',
					'Festive','festive','Festival',
					]
possibles_cities = ['Delhi','delhi','lucknow','Lucknow','lko','Lko','LKO','Noida','noida','mathura','Mathura']

class SearchEmfView(ListView):
	template_name = "search/view.html"

	def get_context_data(self,*args,**kwargs):
		context = super(SearchEmfView,self).get_context_data(*args,**kwargs)
		context['query'] = self.request.GET.get('q')
		# context['noresult'] = False
		return context

	def get_queryset(self,*args,**kwargs): #do all the search logic here
		request = self.request
		button_value = request.GET.get('v')
		print(button_value)
		query = request.GET.get('q') #it can be like "birthday organisers in Lucknow"
		dict = request.GET
		print('query dict is',dict)
		l=list()
		if query is not None:
			w=query.split()
			words = []
			for i in w:
				if i in possibles_cities:
					words.append(i)
			for i in w:
				if i in possibles_events:
					words.append(i)
			print('searching over',words)
			for word in words:
				for i in Emf.objects.filter(city__icontains=word): #then checking for the city
					l.append(i)
					print('adding', i, 'for city', word)
				for i in Emf.objects.filter(specialty__icontains=word): #then check for the specialty
					l.append(i)
					print('adding', i , 'for specialty',word)
			print('returning ',l)
			return list(set(l))
		else:
			print('returning none for result')
			return None
