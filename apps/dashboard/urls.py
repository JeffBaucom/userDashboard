from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'dash_index'),
    url(r'^signin$', views.signin, name = 'dash_signin'),
    url(r'^register$', views.register, name = 'dash_register'),

    # logs into admin's page
    url(r'^dashboard/admin$', views.dash-admin, name = 'dash_admin'),
    url(r'^users/new$', views.users-new, name = 'users_new'),

    # logs into user's page
    url(r'^users/show/(?P<id>\d+)$', views.show-users, name = 'show_user'),

    # only allow admin to edit
    url(r'^users/edit/(?P<id>\d+)$', views.admin-edit, name = 'admin_edit'),
    url(r'^dashboard$', views.dash, name = 'dash'),
    url(r'^users/edit$', views.user-edit, name = 'user_edit')
]
