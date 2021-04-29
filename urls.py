from django.conf.urls import url

from plugins.export import views

urlpatterns = [
    url(r'^manager/$', views.manager, name='export_manager'),
    url(r'^articles/$', views.export_articles, name='export_articles'),
    url(r'^articles/(?P<article_id>\d+)/$',
        views.export_article,
        name='export_article',
        ),
    url(r'^articles/(?P<article_id>\d+)/format/(?P<format>csv|html)/$',
        views.export_article,
        name='export_article',
        ),
    url(r'^articles/all/$', views.export_articles_all, name='export_articles_all'),
]
