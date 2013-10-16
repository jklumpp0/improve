from django.db import models
from django.contrib.auth.models import User

class MetricType(models.Model):
	metric_name = models.CharField(max_length = 30)
	metric_unit = models.CharField(max_length = 10)

	def __unicode__(self):
		return "%s (%s)" % (self.metric_name, self.metric_unit)

class Condition(models.Model):
	user = models.ForeignKey(User)
	metric = models.ForeignKey(MetricType)
	metric_value = models.IntegerField()
	date = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return "%d %s" % (self.metric_value, self.metric)

