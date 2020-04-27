from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Queue, Member, QueueMember, Outcome

class QueueMemberInline(admin.TabularInline):
    model = QueueMember

class QueueAdmin(admin.ModelAdmin):
    inlines = [QueueMemberInline,]

admin.site.register(Queue, QueueAdmin)
admin.site.register(Member)
admin.site.register(QueueMember)
admin.site.register(Outcome)