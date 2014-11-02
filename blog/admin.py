from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from blog.models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}      #Completa el campo slug con el titulo para generar la URL
    list_display = ('title', 'slug' )                      
    search_fields = ('title', 'slug' )
    fieldsets = (                                   #Set fieldsets to control the layout of admin “add” and “change” pages.
        (
            None, 
            {
                'fields': ('title', 'slug')
            }
        ),
    )
    
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'content_markdown' : AdminPagedownWidget(),
        }
        exclude = ['content_markup',]

        
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date_publish')
    search_fields = ('title', 'content_markdown',)
    list_filter = ('categories',)
    fieldsets = (
        (
            None, 
            {
                'fields': ('title', 'slug', 'content_markdown', 'categories', 'date_publish',)
            }
        ),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)