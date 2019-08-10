from django.conf.urls import url , include
from . import views

urlpatterns = [
    #url(r'^custom/', views.custom_response),
    url('^$', views.index, name='index'),
    url('add/', views.add, name='add'),
    url('edit/(?P<tweak_id>[0-9]+)/$', views.edit, name='edit'),
    url('delete/(?P<tweak_id>[0-9]+)/$', views.delete, name='delete'),

]