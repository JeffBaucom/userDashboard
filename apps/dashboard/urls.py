from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'dash_index'),
    url(r'^signin$', views.signin, name = 'dash_signin'),
    url(r'^register$', views.register, name = 'dash_register'),
    url(r'^validate$', views.validate, name = 'validate'),

    # logs into user's page
    url(r'^users/show/(?P<id>\d+)$', views.users_show, name = 'show_user'),

    # logs into admin's page
    url(r'^dashboard/admin$', views.dash_admin, name = 'dash_admin'),
    url(r'^users/new$', views.admin_users_new, name = 'admin_users_new'),
    url(r'^user/remove$', views.admin_remove_user, name = 'admin_remove_user'),

    # only allow admin to edit
    url(r'^users/edit/(?P<id>\d+)$', views.admin_edit, name = 'admin_edit'),
    url(r'^dashboard$', views.dash, name = 'user_dash'),
    url(r'^users/edit$', views.user_edit, name = 'user_edit'),
    url(r'^logout$', views.logout, name = 'logout'),
]
