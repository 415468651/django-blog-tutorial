from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('apps.blog.urls', namespace='blog', app_name='blog')),
    url(r'^usera/', include('apps.usera.urls', namespace='usera', app_name='usera')),
    url(r'', include('apps.community.urls', namespace='community', app_name='community'))
]
