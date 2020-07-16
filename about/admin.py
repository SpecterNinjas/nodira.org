from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'title', 'date_created')
    list_filter = ('email', 'date_created')


admin.site.register(Contact, ContactAdmin)
