from django.contrib import admin
from blog.models import User, Teacher, Student, Admin, Event


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    fieldsets = ((
        None,
        {
            'fields':  (
                'first_name',
                'last_name',
                'username',
                'user_type',
                'email',
                'phone_number',
                'is_staff',
                'is_superuser'
            )
        }
    ),)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ('user_id', 'students_number', 'lessons_held', 'salary')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('user_id', 'lessons_passed', 'lessons_left', 'homeworks_passed')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    model = Admin
    list_display = ('user_id',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('title', 'teacher_id', 'student_id', 'start', 'end')