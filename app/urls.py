from django.conf.urls import url
from django.views.generic.base import TemplateView

import classView
import  views
urlpatterns = [
    url(r'^list/create/',classView.RestaurantCreateView.as_view(),name='newlist'),
    # url(r'^list/(?P<pk>[0-9]+)/menu/(?P<pk1>[0-9]+)/edit/', classView.MenuUpdateView.as_view(), name='menuupdate'),
    # url(r'^list/(?P<pk>[0-9]+)/menu/(?P<pk1>[0-9]+)/delete/', classView.MenuDelete.as_view(), name='menudelete'),
    # url(r'^list/(?P<pk>[0-9]+)/menu/create/', classView.MenuCreateView.as_view(), name='menunew'),
    # url(r'^list/(?P<pk>[0-9]+)/update/',classView.RestauarntUpdateView.as_view(),name='restlistupdate'),
    # url(r'^list/(?P<pk>[0-9]+)/menu/',classView.MenuDetail.as_view(),name='menulist'),
    url(r'^list/menu/(?P<pk>[0-9]+)/edit/', classView.MenuUpdateView.as_view(), name='menuupdate'),
    url(r'^list/menu/(?P<pk>[0-9]+)/delete/', classView.MenuDelete.as_view(), name='menudelete'),
    url(r'^list/menu/create/', classView.MenuCreateView.as_view(), name='menunew'),
    url(r'^list/update/',classView.RestauarntUpdateView.as_view(),name='restlistupdate'),
    url(r'^lists/(?P<pk>[0-9]+)/menu/',classView.MenuList.as_view(),name='menulists'),
    url(r'^list/menu/',classView.MenuDetail.as_view(),name='menulist'),
    url(r'^lists/',classView.RestaurantList.as_view(),name='list'),
    url(r'^list/',classView.RestaurantDetail.as_view(),name='loginlist'),
    url(r'^',TemplateView.as_view(template_name="mainpage.html"),name="main"),
]
# urlpatterns=[
#     url(r'^lists/(?P<pk>[0-9]+)/menu/', views.menus_detail),
#     url(r'^lists', views.rest_list),
#     url(r'^newowner/',views.user_list),
# ]
