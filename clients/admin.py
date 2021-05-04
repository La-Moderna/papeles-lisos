from clients.models import Agent
from clients.models import ClientsBalance

from django.contrib import admin


class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'representant',
        'is_active',
    ]


admin.site.register(Agent, AgentAdmin)


class ClientsBalanceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'orderBalance',
        'factureBalance'
        'is_active',
    ]


admin.site.register(ClientsBalance, ClientsBalanceAdmin)
