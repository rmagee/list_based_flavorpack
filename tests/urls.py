# -*- coding: utf-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2018 SerialLab Corp.  All rights reserved.

from __future__ import unicode_literals, absolute_import

from django.urls import re_path, include

app_name = "list_based_flavorpack"

urlpatterns = [
    re_path(r"^capture/", include("quartet_capture.urls", namespace="quartet-capture")),
    re_path(r"^output/", include("quartet_output.urls", namespace="quartet-output")),
    re_path(r"^serialbox/", include("serialbox.api.urls")),
    re_path(r"^templates/", include("quartet_templates.urls")),
]
