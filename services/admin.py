from django.contrib import admin
from services.models import Service, Option

class OptionInline(admin.TabularInline):
	model = Option
	extra = 0

class ServiceAdmin(admin.ModelAdmin):
	search_fields = ['name']
	inlines = [OptionInline]
	list_display = ('name', 'short_description')

admin.site.register(Service, ServiceAdmin)
