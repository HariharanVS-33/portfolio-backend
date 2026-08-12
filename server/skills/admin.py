from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'category')
    list_editable = ('category', 'order', 'is_active')
