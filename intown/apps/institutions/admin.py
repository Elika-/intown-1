from django.contrib import admin
from .models import Institute
from .models import InstituteOpenHours


class InstituteOpenHoursInline(admin.TabularInline):
    model = InstituteOpenHours


class InstituteAdmin(admin.ModelAdmin):
    inlines = [InstituteOpenHoursInline]


admin.site.register(Institute, InstituteAdmin)
