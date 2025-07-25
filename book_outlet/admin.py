from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address) # if you want to register Address model in the admin panel
admin.site.register(Country)