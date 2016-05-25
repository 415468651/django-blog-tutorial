from django.conf.urls import url
from usera import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signin/$', views.SignInView.as_view(), name='signin'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^password_change/$', views.PassWordChangeView.as_view(), name='password_change'),
    url(r'^profile_change/(?P<pk>[0-9]+)/$', views.ProfileChangeView.as_view(), name='profile_change'),
    url(r'^logout/$', views.log_out, name='log_out'),
]
