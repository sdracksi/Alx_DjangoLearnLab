from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

#Explanation:
#	•	list_display → Displays title, author, and publication_year in the admin list view.
#	•	search_fields → Enables search functionality for title and author.
#	•	list_filter → Allows filtering books by publication_year.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Register the CustomUser model in the Django admin
admin.site.register(CustomUser, CustomUserAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)

# Automatically create user groups
def setup_groups():
    groups = {
        "Editors": ["can_create", "can_edit"],
        "Viewers": ["can_view"],
        "Admins": ["can_create", "can_edit", "can_delete", "can_view"],
    }

    for group_name, permissions in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_codename in permissions:
            permission = Permission.objects.get(codename=perm_codename)
            group.permissions.add(permission)

setup_groups()  # Ensure groups are created on startup