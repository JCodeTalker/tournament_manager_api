from django.contrib import admin
from apps.api.models import Decks, Cards

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cards, AuthorAdmin)
admin.site.register(Decks, AuthorAdmin)
