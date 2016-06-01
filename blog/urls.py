from django.conf.urls import url
from blog import views

urlpatterns = [

    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^blog$', views.IndexView.as_view(), name='index'),
    # url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r"^blog/(?P<article_id>\d+)/(?P<blog_slug>[\w,-]+)$", views.ArticleDetailView.as_view(), name="detail"),
    url(r'^blog/category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_name>[\w,-]+)$', views.TagView.as_view(), name='tag'),
    url(r'^archives', views.ArchiveView.as_view(), name='archives'),
]
