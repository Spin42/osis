##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2016 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
from django.contrib import admin
from django.db import models


class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end')
    fieldsets = ((None, {'fields': ('name', 'date_start', 'date_end')}),)


class Period(models.Model):
    name = models.CharField(max_length=255)
    date_start = models.DateField(blank=False)
    date_end = models.DateField(blank=False)

    def __str__(self):
        return u"%s" % self.name


def search(**kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v}
    return Period.objects.filter(**kwargs).select_related().order_by("date_start")


def find_by_id(period_id):
    return Period.objects.get(pk=period_id)
