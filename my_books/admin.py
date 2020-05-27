from django.contrib import admin

# Register your models here.



from .models import My_books

class My_booksModelAdmin(admin.ModelAdmin):
	list_display=["title","tpublish"]
	list_display_links=["tpublish"]
	list_filter=["tpublish"]
	search_fields=["title","content"]
	list_editable=["title",]

	class My_books:
		model=My_books

admin.site.register(My_books,My_booksModelAdmin)