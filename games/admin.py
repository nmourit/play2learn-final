from django.contrib import admin

from common.admin import Play2LearnAdmin

# Register your models here.
from .models import GameScore

@admin.register(GameScore)
class GameScoreAdmin(Play2LearnAdmin):
    model = GameScore

    # List Attributes
    date_hierarchy = 'created'
    list_display = ['score', 'game', 'settings', 'user_name', 'created']
    ordering = ['-created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('user_name', 'created')
        
        return ()
