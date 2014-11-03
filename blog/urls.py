from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='blog-article-index'),
    url(r'^(?P<slug>[\w\-]+)/$', views.single, name='blog-article-single'),                   
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.date_archive, name='blog-date-archive'),
    url(r'^archive/(?P<slug>[-\w]+)/$', views.category_archive, name='blog-category-archive'),
)
