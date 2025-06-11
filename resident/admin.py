from django.contrib import admin
from .models import Resident
from .models import Testimonio


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user_email', 'identity_document', 'gender', 'phone', 'birth_date')
    search_fields = ('first_name', 'last_name1', 'last_name2', 'identity_document', 'user__email')
    list_filter = ('gender',)

    def full_name(self, obj):
        if obj.last_name2:
            return f"{obj.first_name} {obj.last_name1} {obj.last_name2}"
        return f"{obj.first_name} {obj.last_name1}"
    full_name.short_description = 'Full Name'
    full_name.admin_order_field = 'first_name'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'
    user_email.admin_order_field = 'user__email'




class TestimonioAdmin(admin.ModelAdmin):
    list_display = ('residente', 'fecha', 'aprobado')
    list_filter = ('aprobado',)
    search_fields = ('residente__first_name', 'residente__last_name1', 'comentario')

admin.site.register(Testimonio, TestimonioAdmin)