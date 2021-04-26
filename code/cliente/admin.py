from django.contrib import admin
from .models import Client, Telephone, Email


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class TelephoneInline(admin.TabularInline):
    model = Telephone
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'rg', 'cpf', 'birth_date', 'gender']
    inlines = [EmailInline, TelephoneInline]
    list_display = ('name', 'rg', 'cpf', 'birth_date', 'gender', 'client_age')
    list_filter = ['birth_date']
    search_fields = ['name']


admin.site.register(Client, ClientAdmin)
# admin.site.register(Telephone)
# admin.site.register(Email)






