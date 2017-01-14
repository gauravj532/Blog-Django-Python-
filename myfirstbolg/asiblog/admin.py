from django.contrib import admin
from . import models
from .models import Post,Tag

class TagInline(admin.TabularInline):
	model = Tag.post.through
	extra=0

class PostAdmin(admin.ModelAdmin):
	fields = ['title','body','publish',]
	readonly_fields = ['created','modified']
	list_display =('title','publish','created','modified')
	inlines = [
        TagInline,
    ]
class TagAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    exclude = ('post',)

admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
