from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                    
    url(r'^blog/', include('blog.urls', namespace='blog')),                     

    url(r'^markdown/', include( 'django_markdown.urls')),                   
                       
    url(r'^admin/', include(admin.site.urls)),
)
