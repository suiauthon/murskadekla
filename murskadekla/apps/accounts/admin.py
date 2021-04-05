from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import EmailActivation

User = get_user_model()

admin.site.register(User)

class EmailActivationAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = EmailActivation


admin.site.register(EmailActivation, EmailActivationAdmin)
