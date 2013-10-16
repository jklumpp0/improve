from django.contrib import admin
from .models import MetricType, Condition

class ConditionAdmin(admin.ModelAdmin):
	readonly_fields = ['date']
	fieldsets = [
			(None, {'fields': ['user',]}),
			('Condition', {'fields': ['metric_value', 'metric', 'date']})
	]

admin.site.register(MetricType)
admin.site.register(Condition, ConditionAdmin)


