from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
	user = models.ForeignKey(User, default = User.objects.all()[0])
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)

	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)

class MetricType(models.Model):
	metric_name = models.CharField(max_length = 30)
	metric_unit = models.CharField(max_length = 10)

	def __unicode__(self):
		return "%s (%s)" % (self.metric_name, self.metric_unit)

class Condition(models.Model):
	person = models.ForeignKey(Person)
	metric = models.ForeignKey(MetricType)
	metric_value = models.IntegerField()
	date = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return "%d %s" % (self.metric_value, self.metric)

