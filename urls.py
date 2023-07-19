from django.urls import re_path

from plugins.export import views

urlpatterns = [
    re_path(r'^manager/$', views.manager, name='export_manager'),
    re_path(r'^articles/$', views.export_articles, name='export_articles'),
    re_path(r'^articles/(?P<article_id>\d+)/$',
        views.export_article,
        name='export_article',
        ),
    re_path(r'^articles/(?P<article_id>\d+)/format/(?P<format>csv|html)/$',
        views.export_article,
        name='export_article',
        ),
    re_path(r'^articles/all/$', views.export_articles_all, name='export_articles_all'),
]
