from django.contrib import admin
from books.models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('AuthorId', 'Name', 'Age','Country')
    search_fields = ('AuthorId', 'Name')
class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'Title', 'PublishDate')
    list_filter = ('PublishDate',)
    date_hierarchy = 'PublishDate'
    ordering = ('-PublishDate',)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
