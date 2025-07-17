from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Produto, Entrega 

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Função no Sistema', {'fields': ('role',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'role']
    list_filter = UserAdmin.list_filter + ('role',)


admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco']

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ['id', 'destinatario', 'cliente', 'entregador_atribuido', 'status', 'data_criacao']
    list_filter = ['status', 'data_criacao']
