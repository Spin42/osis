##############################################################################
#
# OSIS stands for Open Student Information System. It's an application
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
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
from base.models import learning_unit_enrollment
import datetime


def create_date_enrollment():
    return datetime.date.today()


def create_learning_unit_enrollment(learning_unit_year, offer_enrollment):
    a_learning_unit_enrollment = \
        learning_unit_enrollment.LearningUnitEnrollment(date_enrollment=create_date_enrollment(),
                                                        learning_unit_year=learning_unit_year,
                                                        offer_enrollment=offer_enrollment)
    a_learning_unit_enrollment.save()
    return a_learning_unit_enrollment
