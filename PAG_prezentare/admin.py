from django.contrib import admin
from .models import Prezentare  

class PrezentareAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)


admin.site.register(Prezentare, PrezentareAdmin)

