from django.db import models

from markdown import markdown

class Category(models.Model) :
    
    title = models.CharField(max_length = 255)
    slug = models.SlugField(
        verbose_name = 'Slug',
        help_text = 'Uri identifier.',
        max_length = 255,
        unique = True
    )
    
    class Meta:
        app_label = 'blog'
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title',]
    
    def __str__(self):
        return "%s" % (self.title,) #Convert to string.

class Article(models.Model) :
    
    title = models.CharField(max_length = 255)
    slug = models.SlugField(
        verbose_name = 'Slug',
        help_text = 'Uri identifier.',
        max_length = 255,
        unique = True
    )
    content_markdown = models.TextField(
        verbose_name = 'Content (Markdown)',
    )
    content_markup = models.TextField(
        verbose_name = 'Content (Markup)',
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name = 'Categories',
        null = True,
        blank = True
    )
    date_publish = models.DateTimeField(
        verbose_name = 'Publish Date',
    )
    
    class Meta:
        app_label = 'blog'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-date_publish']
        
    def save(self):
        self.content_markup = markdown(self.content_markdown, ['codehilite'])
        super(Article, self).save()
        
    def __str__(self):
        return "%s" % (self.title,) #Convert to string.
        
        
