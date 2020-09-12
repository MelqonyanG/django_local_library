from django.contrib import admin
from .models import Book, BookInstance, Author, Genre, Language

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookInstanceInLine(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInLine]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back', 'borrower')

    fieldsets = (
        (
            None, {
                'fields': ('book', 'imprint', 'id')
            }
        ),
        (
            'Availability', {
                'fields': ('status', 'due_back', 'borrower')
            }
        )
    )
