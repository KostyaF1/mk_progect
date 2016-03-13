from django.contrib import admin
from managers.models import Manager
from django.contrib.auth.models import User

class ManagerAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'get_full_name', 'gender', 'skype', 'description', 'second_position', 'main_position')
	list_filter = ['user__is_staff']
	search_fields = ['user__first_name', 'user__last_name', 'gender', 'skype', 'description']

admin.site.register(Manager, ManagerAdmin)
