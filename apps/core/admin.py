from django.contrib import admin

from core.models import Entry, LightningTalk, News, Session
from core.views import get_username


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', '_username', 'email', 'description')

    def _username(self, obj):
        provider, username = get_username(obj.user)
        return '{} ({})'.format(username, provider)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')


class LightningTalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'created_at', 'is_active', 'order')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'created_at', 'is_keynote', 'is_short_session', 'is_active', 'order')


admin.site.register(Entry, EntryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(LightningTalk, LightningTalkAdmin)
admin.site.register(Session, SessionAdmin)
