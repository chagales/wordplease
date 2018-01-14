from django.contrib import admin

from blogging.models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'user', 'intro', 'publication_date')
    list_filter = ('category',)
    search_fields = ('id', 'title', 'user')


admin.site.register(Post, PostAdmin)
