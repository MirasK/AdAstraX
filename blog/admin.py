from django.contrib import admin
from blog.models import User, Teacher, Student, Admin


admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Admin)

class UserAdmin(admin.ModelAdmin):

    list_display = ("username", "email")