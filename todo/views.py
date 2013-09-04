from django.http import HttpResponse
from django.template import RequestContext, loader

def home(request):
	template = loader.get_template('todo/home.html')
	context = RequestContext(request, { 'name': 'World' })
	return HttpResponse(template.render(context))

