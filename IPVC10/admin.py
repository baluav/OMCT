from django.contrib import admin

# Register your models here.
from .models import Patashala, Student, Register

# Register your models here.
class PatashalaAdmin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_display = ('name', 'address', 'city', 'state', 'phone1')
    list_filter = ('state', 'city')
    fields = ['name', 'address', ('city', 'state', 'pincode'), ('phone1', 'phone2'), 'number_of_students']

admin.site.register(Patashala, PatashalaAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'patashala')
    list_filter = ('patashala', 'name')

admin.site.register(Student, StudentAdmin)

class RegisterAdmin(admin.ModelAdmin):
    date_hierarchy = 'dor'

admin.site.register(Register, RegisterAdmin)
