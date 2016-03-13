# -*- coding: utf-8 -*- 
from django.contrib import admin
from masters.models import Master, Position

class MasterAdmin(admin.ModelAdmin):
	filter_horizontal = ('services',)
	fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth', 'passport']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        ('Master of', {'fields':['services', 'main_position', 'second_position']}),
    ]
	list_filter = ['services']
	search_fields = ['surname', 'email']
	list_display = ['full_name', 'phone', 'main_position', 'second_position']

admin.site.register(Master, MasterAdmin)
admin.site.register(Position)
