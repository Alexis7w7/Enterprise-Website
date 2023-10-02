from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'author', 'post_categories')
    ordering = ('author',)
    search_fields = ('title', 'author__username', 'categories__name')
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ",".join([c.name for c in obj.categories.all().order_by('name')])

    post_categories.short_description = "Category"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
