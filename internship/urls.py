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
from django.conf.urls import url

from internship.views import home, internship, master, period, place, speciality, student, student_resume
from internship import upload_xls

urlpatterns = [
    # S'il vous plaît, organiser les urls par ordre alphabétique.
    url(r'^$', home.internships_home, name='internships_home'),
    url(r'^internships/$', internship.internships, name='internships'),
    url(r'^internships/([0-9]+)/students/$', internship.student_choice, name='internship_detail_student_choice'),
    url(r'^internships/block/$', internship.internships_block, name='internships_block'),
    url(r'^internships/save/$', internship.internships_save, name='internships_save'),
    url(r'^internships/save/modifications/student/$', internship.internship_save_modification_student, name='internship_save_modification_student'),
    url(r'^internships/std/$', internship.internships_stud, name='internships_stud'),
    url(r'^internships/student/([0-9]+)/edit/$', internship.internships_modification_student, name='internships_modification_student'),
    url(r'^internships/upload/$', upload_xls.upload_internships_file,name='upload_internship'),

    url(r'^internships_masters/$', master.interships_masters, name='interships_masters'),
    url(r'^internships_masters/delete/$', master.delete_interships_masters, name='delete_interships_masters'),
    url(r'^internships_masters/upload/$', upload_xls.upload_masters_file, name='upload_interships_masters'),

    url(r'^periods/$', period.internships_periods, name='internships_periods'),
    url(r'^periods/create/$', period.period_create, name='periods_create'),
    url(r'^periods/new/$', period.period_new, name='periods_new'),

    url(r'^places/$', place.internships_places, name='internships_places'),
    url(r'^places/([0-9]+)/students/$', place.student_choice, name='place_detail_student_choice'),
    url(r'^places/create/$', place.organization_create, name='place_create'),
    url(r'^places/edit/([0-9]+)/$', place.organization_edit, name='place_edit'),
    url(r'^places/save/([0-9]+)/([0-9]+)/$', place.place_save, name='place_save'),
    url(r'^places/save/$', place.organization_new, name='place_save_new'),
    url(r'^places/std/$', place.internships_places_stud, name='internships_places_stud'),
    url(r'^places/upload/$', upload_xls.upload_places_file,name='upload_places'),

    url(r'^specialities/$', speciality.specialities, name='internships_specialities'),
    url(r'^specialities/create/$', speciality.speciality_create, name='speciality_create'),
    url(r'^specialities/new/$', speciality.speciality_new, name='speciality_new'),

    url(r'^students/([0-9]+)/information/edit/$', student_resume.internship_student_information_modification, name='internship_student_information_modification'),
    url(r'^students/([0-9]+)/sumup/$', student_resume.internships_student_read, name='internships_student_read'),
    url(r'^students/([0-9]+)/save/information/$', student_resume.student_save_information_modification, name='student_save_information_modification'),
    url(r'^students/sumup/$', student_resume.internships_student_resume, name='internships_student_resume'),
    url(r'^students/search$', student_resume.internships_student_search, name='internships_student_search'),

]
