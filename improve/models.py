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
    date = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        import datetime
        super(Condition, self).__init__(*args, **kwargs)
        date = datetime.datetime.now()

    def __unicode__(self):
        return "%d %s" % (self.metric_value, self.metric)

