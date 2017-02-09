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
import csv
from django.contrib.auth.models import Group
from django.db import IntegrityError, DataError
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from base import models as mdl
from internship import models as mdl_internship
from internship.views.internship import sort_internships, set_student_choices_list, get_number_choices, \
    get_all_specialities, get_selectable, set_tabs_name


@login_required
@permission_required('internship.is_internship_manager', raise_exception=True)
# To be removed once all students are imported.
def load_internship_students():
    with open('internship/views/internship_students.csv') as csvfile:
        row = csv.reader(csvfile)
        imported_counter = 0
        error_counter = 0
        duplication_counter = 0
        for columns in row:
            if len(columns) > 0:
                person = mdl.person.find_by_global_id(columns[1].strip())
                if person:
                    internships_student = mdl_internship.InternshipStudentInformation()
                    internships_student.person = person
                    internships_student.location = columns[2].strip()
                    internships_student.postal_code = columns[3].strip()
                    internships_student.city = columns[4].strip()
                    internships_student.country = columns[5].strip()
                    internships_student.phone_mobile = columns[6].strip()
                    internships_student.email = columns[7].strip()
                    try:
                        internships_student.save()
                    except IntegrityError:
                        print("Duplicate : {} - {}".format(str(person), columns[1].strip()))
                        duplication_counter += 1
                    except DataError:
                        error_counter += 1
                        print("Data error : {} - {}".format(str(person), columns[1].strip()))
                    if person.user :
                        intern_students_group = Group.objects.get(name='internship_students')
                        person.user.groups.add(intern_students_group)
                    imported_counter += 1
                else:
                    error_counter += 1
                    print("Erreur : {} - {}".format(columns[0],columns[1]))
        print("Imports : {}".format(imported_counter))
        print("Erreur de données : {}".format(error_counter))
        print("Duplication : {}".format(duplication_counter))


def display_internships_selection(request):
    NUMBER_NON_MANDATORY_INTERNSHIPS = 6
    specialities = mdl_internship.internship_speciality.InternshipSpeciality.objects.all()
    internships_offers = mdl_internship.internship_offer.InternshipOffer.objects.all()
    return render(request, "internships_student_selection.html",
                  {"number_non_mandatory_internships": range(1, NUMBER_NON_MANDATORY_INTERNSHIPS + 1),
                   "specialities": specialities,
                   "internships_offers": internships_offers})


@login_required
@permission_required('internship.can_access_internship', raise_exception=True)
def internships_stud(request):
    # Set the number of non mandatory internship and the sort array depending
    size_non_mandatory = 5
    speciality_sort_value = [None] * size_non_mandatory

    # Check if there is a speciality selected in a tab of non mandatory internship
    if request.method == 'GET':
        for x in range(1,size_non_mandatory):
            if request.GET.get("speciality_sort"+str(x)) != '0':
                speciality_sort_value[x] = request.GET.get("speciality_sort"+str(x))
            else :
                speciality_sort_value[x] = None

    # Get the student base on the user
    student = mdl.student.find_by(person_username=request.user)
    # Get in descending order the student's choices in first lines
    student_choice = mdl_internship.internship_choice.find_by_student_desc(student)

    # Select all Internship Offer
    query = mdl_internship.internship_offer.find_internships()

    # Sort the internships by the organization's reference
    query = sort_internships(query)

    # Change the query into a list
    query = list(query)
    # Delete the internships in query when they are in the student's selection then rebuild the query
    # Put datas wich need to be save in the student's choice list
    query = set_student_choices_list(query, student_choice)
    # Insert the student choice into the global query, at first position,
    for choice in student_choice:
        query.insert(0, choice)

    # Get The number of differents choices for the internships
    get_number_choices(query)

    all_internships = mdl_internship.internship_offer.find_internships()
    all_speciality = get_all_specialities(all_internships)
    selectable = get_selectable(all_internships)
    set_tabs_name(all_speciality, student)

    # Set all non mandatory speciality for the dropdown list
    all_non_mandatory_speciality = mdl_internship.internship_speciality.find_non_mandatory()
    # Create an array of the number of non mandatory internship and put all the internship of the speciality selected in
    all_non_mandatory_internships = [None] * size_non_mandatory
    all_non_mandatory_selected_internships = [None] * size_non_mandatory
    for x in range(0,size_non_mandatory):
        if speciality_sort_value[x]:
            all_non_mandatory_internships[x] = mdl_internship.internship_offer.find_non_mandatory_internships(speciality__name=speciality_sort_value[x])
            get_number_choices(all_non_mandatory_internships[x])
            set_tabs_name(all_non_mandatory_internships[x])
        else:
            all_non_mandatory_internships[x] = None
        all_non_mandatory_selected_internships[x]=mdl_internship.internship_choice.search(internship_choice=x+1)

    return render(request, "internships_stud.html", {'section': 'internship',
                                                     'all_internships': query,
                                                     'non_mandatory_speciality': all_non_mandatory_speciality,
                                                     'all_non_mandatory_internships': all_non_mandatory_internships,
                                                     'all_non_mandatory_selected_internships': all_non_mandatory_selected_internships,
                                                     'speciality_sort_value': speciality_sort_value,
                                                     'all_speciality': all_speciality,
                                                     'selectable': selectable,
                                                     })