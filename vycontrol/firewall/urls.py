from django.urls import path

from . import views

app_name = 'firewall'



urlpatterns = [
    path('', views.index, name='firewall-list'),
    path('show/<str:firewall_name>', views.show, name='show'),
    path('firewall-create', views.create, name='firewall-create'),
    path('firewall-remove/<str:firewall_name>', views.firewall_remove, name='firewall-remove'),
    path('firewall-edit/<str:firewall_name>', views.firewall_edit, name='firewall-edit'),
    path('firewall-config/<str:firewall_name>', views.firewall_config, name='firewall-config'),
    path('firewall-global', views.firewall_global, name='firewall-global'),

    path('firewall-addressgroup-list', views.firewall_addressgroup_list, name='firewall-addressgroup-list'),
    path('firewall-addressgroup-add', views.firewall_addressgroup_add, name='firewall-addressgroup-add'),
    path('firewall-addressgroup-del/<str:groupname>', views.firewall_addressgroup_del, name='firewall-addressgroup-del'),
    path('firewall-addressgroup-desc/<str:groupname>', views.firewall_addressgroup_desc, name='firewall-addressgroup-desc'),

    path('firewall-networkgroup-list', views.firewall_networkgroup_list, name='firewall-networkgroup-list'),
    path('firewall-networkgroup-add', views.firewall_networkgroup_add, name='firewall-networkgroup-add'),
    path('firewall-networkgroup-del/<str:groupname>', views.firewall_networkgroup_del, name='firewall-networkgroup-del'),
    path('firewall-networkgroup-desc/<str:groupname>', views.firewall_networkgroup_desc, name='firewall-networkgroup-desc'),    

    path('firewall-portgroup-list', views.firewall_portgroup_list, name='firewall-portgroup-list'),
    path('firewall-portgroup-add', views.firewall_portgroup_add, name='firewall-portgroup-add'),
    path('firewall-portgroup-del/<str:groupname>', views.firewall_portgroup_del, name='firewall-portgroup-del'),
    path('firewall-portgroup-edit/<str:groupname>', views.firewall_portgroup_edit, name='firewall-portgroup-edit'),

    path('zones', views.firewall_zones, name='firewall-zones'),
    path('zones/add', views.firewall_zones_add, name='firewall-zones-add'),
    path('zones/addrule', views.firewall_zones_addrule, name='firewall-zones-addrule'),
    path('zones/removerule/<str:dstzone>/<str:srczone>/<str:firewall>', views.firewall_zones_removerule, name='firewall-zones-removerule'),
    path('zones/edit/<str:zonename>', views.firewall_zones_edit, name='firewall-zones-edit'),
    path('zones/remove/<str:zonename>', views.firewall_zones_remove, name='firewall-zones-remove'),


    path('addrule/<str:firewall_name>', views.addrule, name='addrule'),
    path('editrule/<str:firewall_name>/<str:rulenumber>', views.editrule, name='editrule'),
    path('firewall-removerule/<str:firewall_name>/<str:firewall_rulenumber>', views.firewall_removerule, name='firewall-removerule'),    

]


