from django.contrib import admin
from blog.models import User

class UserAdmin(admin.ModelAdmin):
    model = User
    fieldsets = ((
        'UserFields',
        {
            'fields':  (
                'first name',
                'last name',
                'username',
                'user_type',
                'email',
            )
        }
    ),)
    exclude = ['email']