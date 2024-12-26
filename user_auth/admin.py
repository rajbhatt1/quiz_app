from django.contrib import admin  
from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin  

User = get_user_model()
# Register your models here.  
class CustomUserAdmin(UserAdmin):  
    
    model = User  
  
    list_display = ('email', 'is_staff', 'is_active',)  
    list_filter = ('email', 'is_staff', 'is_active',)  
    fieldsets = (  
        (None, {'fields': ('email', 'password')}),  
        ('Permissions', {'fields': ('is_staff', 'is_active')}),  
    )  
    add_fieldsets = (  
        (None, {  
            'classes': ('wide',),  
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}  
        ),  
    )  
    search_fields = ('email',)  
    ordering = ('email',)  
    filter_horizontal = ()  
  
admin.site.register(User, CustomUserAdmin)  
