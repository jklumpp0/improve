from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from django.utils.decorators import method_decorator
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView
from django import forms
from .models import Condition, MetricType
from django.contrib.auth.models import User
import logging

logger = logging.getLogger('improve.views')

def test_manual_view(request):
    if request.method == 'POST':
        logger.info('Received: %s, value: %s' % (request.POST, request.POST['first_name']))
        return HttpResponseRedirect(reverse('manual_view'))
    else:
        template = loader.get_template('improve/manual.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))        

def test_view(request):
    context = RequestContext(request, {"name": "Jared"})
    template = loader.get_template('improve/index.html')
    return HttpResponse(template.render(context))

class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ('metric', 'metric_value')

class ConditionTypeForm(forms.ModelForm):
    class Meta:
        model = MetricType

class NameEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

@login_required(login_url = '/improve/login')
def edit_user_view(request):
    if request.method == 'POST':
        form = NameEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('edit_user'))
    else:
        form = NameEditForm(instance = request.user)
        template = loader.get_template('improve/edit_name.html')
        context = RequestContext(request, {'form': form})
        return HttpResponse(template.render(context))

@login_required(login_url = '/improve/login')
def create_type_view(request):
    if request.method == 'POST':
        form = ConditionTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('condition_types'))
    else:
        form = ConditionTypeForm()
        return render(request, 'improve/create_type.html',
                        { 'form': form,
                          'object_list': MetricType.objects.all() })

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
        conditions = Condition.objects \
                              .filter(user = self.request.user) \
                              .order_by("-date")

        # Convert the list of conditions to a dictionary by condition type
        from collections import defaultdict
        conditions_by_type = defaultdict(list)
        for condition in conditions:
            conditions_by_type[condition.metric].append(condition)

        kwargs['s'] = CreateConditionView.success_url
        kwargs['object_list'] = dict(conditions_by_type)
        kwargs['request'] = self.request
        return super(CreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        tmp_condition = Condition(user = self.request.user)
        form = ConditionForm(self.request.POST, instance = tmp_condition)
        return super(CreateConditionView, self).form_valid(form)

    @method_decorator(login_required(login_url="/improve/login/"))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

