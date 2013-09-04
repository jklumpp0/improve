from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django import forms
from .models import Condition, Person

def test_view(request):
	context = RequestContext(request, {"name": "Jared"})
	template = loader.get_template('improve/index.html')
	return HttpResponse(template.render(context))

class ConditionForm(forms.ModelForm):
	class Meta:
		model = Condition

class CreateConditionView(CreateView):
	template_name = 'improve/create_condition.html'
	form_class = ConditionForm

	def get_success_url(self):
		return reverse_lazy('condition')

	def get_initial(self):
		return {
			'person': Person.objects.filter(user = self.request.user)[0]
		}

	def get_context_data(self, **kwargs):
		persons = Person.objects.filter(user = self.request.user)
		objects = []

		for person in persons:
			objects.extend(Condition.objects.filter(person = person))
		kwargs['s'] = CreateConditionView.success_url		
		kwargs['object_list'] = objects
		kwargs['request'] = self.request
		return super(CreateView, self).get_context_data(**kwargs)

	@method_decorator(login_required(login_url="/improve/login/"))
	def dispatch(self, *args, **kwargs):
		return super(CreateView, self).dispatch(*args, **kwargs)

