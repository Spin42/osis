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


class PeriodInternshipPlacesAdmin(admin.ModelAdmin):
    list_display = ('period', 'internship', 'number_places')
    fieldsets = ((None, {'fields': ('period', 'internship', 'number_places')}),)
    raw_id_fields = ('period', 'internship')


class PeriodInternshipPlaces(models.Model):
    period = models.ForeignKey('internship.Period')
    internship = models.ForeignKey('internship.InternshipOffer')
    number_places = models.IntegerField(blank=None, null=False)


def search(**kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v}
    return PeriodInternshipPlaces.objects.filter(**kwargs).select_related("period", "internship")


def find_by_id(id):
    return PeriodInternshipPlaces.objects.get(pk=id)
