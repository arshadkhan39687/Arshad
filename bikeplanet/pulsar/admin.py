from django.contrib import admin

from .models import Bikes, Next

class BikesAdmin(admin.ModelAdmin):
	fieldsets = [
        ('BIKE REVIEW', {'fields': ['bike_name']}),
        (None, {'fields': ['launch_date']}),
		(None, {'fields': ['bike_desc']}),
		(None, {'fields': ['review']}),
    ]
	list_display = ('bike_name', 'launch_date', 'bike_desc', 'review')
	list_filter = ['bike_name']
	search_fields = ['bike_name']

class NextAdmin(admin.ModelAdmin):
	fieldsets = [
        ('BIKE REVIEW', {'fields': ['bike_name']}),
        (None, {'fields': ['launch_date']}),
		(None, {'fields': ['bike_desc']}),
		(None, {'fields': ['review']}),
    ]
	list_display = ('bike_name', 'launch_date', 'bike_desc', 'review')
	list_filter = ['bike_name']
	search_fields = ['bike_name']




admin.site.register(Bikes, BikesAdmin)
admin.site.register(Next, NextAdmin)

