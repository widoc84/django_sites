from django.contrib import admin

from .models import Imployee, VacationDate


class ImployeeAdmin(admin.ModelAdmin):
    list_display = ('id_redmine', 'name', 'is_enabled',)
    list_display_links = ('id_redmine',)
    search_fields = ('name', 'id_redmine',)
    list_editable = ('is_enabled',)
    list_filter = ('name', 'id_redmine',)

class VacationAdmin(admin.ModelAdmin):
    list_display = ('date_start', 'date_finish', 'reason', 'imployee')
    list_display_links = ('date_start', 'date_finish', 'reason', 'imployee')

admin.site.register(Imployee, ImployeeAdmin)
admin.site.register(VacationDate, VacationAdmin)
