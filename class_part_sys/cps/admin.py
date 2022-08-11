from django.contrib import admin

from .models import Student, Module, Session, ClassParticipation

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "student_id", "name")

class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "module_code", "name", "section_id")

admin.site.register(Student, StudentAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Session)
admin.site.register(ClassParticipation)
