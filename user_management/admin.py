from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import TodoUserProfile

class TodoUserProfileInline(admin.StackedInline):
    model = TodoUserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'
    
# Define a new User admin    
class TodoUserAdmin(UserAdmin):
    inlines = (TodoUserProfileInline, )    
    
    
admin.site.unregister(User)
admin.site.register(User, TodoUserAdmin)    