from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from django.utils.decorators import method_decorator
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView
from django import forms
from .models import Condition

def test_view(request):
    context = RequestContext(request, {"name": "Jared"})
    template = loader.get_template('improve/index.html')
    return HttpResponse(template.render(context))

class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ('metric', 'metric_value')

class CreateConditionView(CreateView):
    template_name = 'improve/create_condition.html'
    form_class = ConditionForm

    def get_success_url(self):
        return reverse_lazy('condition')

    def get_initial(self):
        return {
            'person': self.request.user
        }

    def get_context_data(self, **kwargs):
        objects = Condition.objects.filter(user = self.request.user)

        kwargs['s'] = CreateConditionView.success_url
        kwargs['object_list'] = objects
        kwargs['request'] = self.request
        return super(CreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        tmp_condition = Condition(user = self.request.user)
        form = ConditionForm(self.request.POST, instance = tmp_condition)
        return super(CreateConditionView, self).form_valid(form)

    @method_decorator(login_required(login_url="/improve/login/"))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

