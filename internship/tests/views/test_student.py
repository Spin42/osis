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
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from internship.views import student
from base.tests.models import test_student


class StudentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user("user", "user@test.com", "pass")
        permission = Permission.objects.get(codename="can_access_internship")
        self.user.user_permissions.add(permission)
        self.student = test_student.create_student("stud", "std", "45451214")
        self.student.person.user = self.user
        self.student.person.save()

    def test_access_internship_offers_selection(self):
        url = reverse(student.display_internships_selection)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
