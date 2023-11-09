from django.contrib import admin

from emailserv.models import Emailserv, Message


# Register your models here.
@admin.register(Emailserv)
class EmailservAdmin(admin.ModelAdmin):
    fields = ('emails', 'time', 'period', 'message')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ('title', 'body')