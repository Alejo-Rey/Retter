from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'picture')

    list_editable = ('phone_number', 'picture')

    search_fields = (
        'user',
        'user__first_name', 
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created', 
        'modified',
        )

    fieldsets = (
        # Primer elemento es la categoria
        ('Profile', {
            'fields': (
                ('user', 'picture'),),
            
        }),
        ('Extra info', {
            'fields': (
                ('phone_number',),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified')
            )
        })
    )
    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    
    model = Profile
    can_delete = False
    verbose_name = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    
    
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)