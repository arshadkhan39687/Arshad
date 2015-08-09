from django.shortcuts import render
from .models import Bikes, Next
from django.http import HttpResponse
from django.template import loader, RequestContext

def index(request):
	bikes_list = Bikes.objects.all()
	next_list = Next.objects.all()
	#bikes_obj = Bikes.objects.get(bike_name = name)
	#next_obj = Next.objects.get(bike_name = name)
	template =  loader.get_template('admin/arshad.html')
	context = RequestContext(request, {'bikes_list': bikes_list, 'next_list': next_list,})
	return HttpResponse(template.render(context))


	

	
	
def specificbike(request, name):
	bikes_list = Bikes.objects.all()
	next_list = Next.objects.all()
	bikes_obj = Bikes.objects.get(bike_name = name)
	#next_obj = Next.objects.get(bike_name = name)
	template =  loader.get_template('admin/sbike.html')
	context = RequestContext(request, {'bikes_obj': bikes_obj, 'bikes_list': bikes_list, 'next_list': next_list,})
	return HttpResponse(template.render(context))



	
