"""
    Copyright 2018 SerialLab, CORP

    This file is part of ListBasedFlavorpack.

    RandomFlavorpack is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    RandomFlavorpack is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with RandomFlavorpack.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.urls import re_path
from list_based_flavorpack.api import views
from list_based_flavorpack.api import viewsets
from list_based_flavorpack.api.routers import urlpatterns as router_urlpatterns

urlpatterns = [
    re_path(
        r"^list-based-regions/$",
        viewsets.list_based_region_list,
        name="list-based-region-list",
    ),
    re_path(
        r"^list-based-region-create/$",
        viewsets.list_based_region_create,
        name="list-based-region-create",
    ),
    re_path(
        r"^list-based-region-detail/(?P<machine_name>[\w\-\_]{1,100})/$",
        viewsets.list_based_region_detail,
        name="list-based-region-detail",
    ),
    re_path(
        r"^list-based-region-modify/(?P<machine_name>[\w\-\_]{1,100})/$",
        viewsets.list_based_region_modify,
        name="list-based-region-modify",
    ),
    re_path(
        r"^list-based-region-form/(?P<machine_name>[\w\-\_]{1,100})/$",
        viewsets.list_based_region_form,
        name="list-based-region-form",
    ),
    re_path(
        r"^clone-list-based-pool/$",
        views.CloneListBasedFlavorpackView.as_view(),
        name="clone-pool",
    ),
    re_path(
        r"^clone-list-based-pool/(?P<machine_name>[\w\-\_]{1,100})/(?P<new_machine_name>[\w\-\_]{1,100})/$",
        views.CloneListBasedFlavorpackView.as_view(),
        name="clone-pool-view",
    ),
] + router_urlpatterns
