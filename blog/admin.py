from django.contrib import admin
from blog.models import User, Teacher, Student, Admin


@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'email')
    fieldsets = ((
        None,
        {
            'fields':  (
                'first_name'
                'last_name',
                'username',
                'user_type',
                'email',
                'phone_number'
            )
        }
    ),)

@admin.register(Teacher)

class TeacherAdmin(admin.ModelAdmin):
    pass