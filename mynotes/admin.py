from django.contrib import admin
from .models import Category, Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'noter', 'description', 'category')
    list_filter = ('date', 'category')
    search_fields = ('noter', 'category', 'name', 'description')

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category')
        }),
        ('User', {
            'fields': ('date', 'noter')
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)


