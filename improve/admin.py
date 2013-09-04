from django.contrib import admin
from .models import Person, MetricType, Condition

class ConditionAdmin(admin.ModelAdmin):
	readonly_fields = ['date']
	fieldsets = [
			(None, {'fields': ['person',]}),
			('Condition', {'fields': ['metric_value', 'metric', 'date']})
	]

admin.site.register([Person, MetricType])
admin.site.register(Condition, ConditionAdmin)


