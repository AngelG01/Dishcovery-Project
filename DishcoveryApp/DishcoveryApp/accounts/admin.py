from django.contrib import admin
from django.contrib.auth import get_user_model

from DishcoveryApp.accounts.forms import UserProfileCreationForm, UserProfileChangeForm

UserModel = get_user_model()


# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    model = UserModel
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser',)
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
