import json
from datetime import time
from deisicourses.models import Course, Branch, CurricularUnit, Teacher

with open('deisicourses/json/lei_info.json', encoding='utf-8') as lei_file:
    data = json.load(lei_file)

    course_flat_plan = data.get('courseFlatPlan', [])
    course_detail = data.get('courseDetail', {})

    course_name = course_detail.get('courseName')
    direction_contact = course_detail.get('directionContact')

    # Ensure the Teacher object exists or create it
    director = None
    if direction_contact:
        try:
            director = Teacher.objects.get(name=direction_contact)
        except Teacher.DoesNotExist:
            director = Teacher(name=direction_contact)
            director.save()

    # Ensure the Course object exists or create it
    try:
        course = Course.objects.get(name=course_name)
    except Course.DoesNotExist:
        course = Course(
            name=course_name,
            presentation=course_detail.get('presentation'),
            objectives=course_detail.get('objectives'),
            competences=course_detail.get('competences'),
            scientific_area=course_detail.get('scientificArea'),
            director=director,
            deliberation=course_detail.get('A3ESDeliberation'),
            career_opportunities=course_detail.get('careerOportunities')
        )
        course.save()

    # Update the Course object if it already exists
    course.presentation = course_detail.get('presentation')
    course.objectives = course_detail.get('objectives')
    course.competences = course_detail.get('competences')
    course.scientific_area = course_detail.get('scientificArea')
    course.director = director
    course.deliberation = course_detail.get('A3ESDeliberation')
    course.career_opportunities = course_detail.get('careerOportunities')
    course.save()

    # CURRICULAR UNITS #
    for curUnit_details in course_flat_plan:
        try:
            curricular_unit = CurricularUnit.objects.get(name=curUnit_details['curricularUnitName'])
        except CurricularUnit.DoesNotExist:
            # Handle time format conversion
            hr_total_contacto = curUnit_details.get('hrTotalContacto', '00:00:00')
            try:
                hours, minutes = map(int, hr_total_contacto.split(':'))
                time_spent = time(hour=hours, minute=minutes)
            except ValueError:
                time_spent = time(hour=0, minute=0)

            # Ensure all required fields are set before creating the CurricularUnit object
            curricular_unit = CurricularUnit(
                name=curUnit_details['curricularUnitName'],
                year=curUnit_details.get('curricularYear'),
                semester=curUnit_details.get('semester'),
                ects=curUnit_details.get('ects'),
                cu_readable_code=curUnit_details.get('curricularIUnitReadableCode', ''),
                time_spent=time_spent,  # Assuming this field is required, you might want to fill this from your data
                course=course  # Assign the course during creation
            )

            try:
                cur_branch = Branch.objects.get(name=curUnit_details['curricularBranchName'])
            except Branch.DoesNotExist:
                cur_branch = Branch(name=curUnit_details['curricularBranchName'])
                cur_branch.save()

            curricular_unit.cu_branch = cur_branch
            curricular_unit.save()
        else:
            # If the curricular unit already exists, add it to the course if not already added
            if not course.curricular_units.filter(pk=curricular_unit.pk).exists():
                course.curricular_units.add(curricular_unit)

        # Update the CurricularUnit object if it already exists
        curricular_unit.year = curUnit_details.get('curricularYear')
        curricular_unit.semester = curUnit_details.get('semester')
        curricular_unit.ects = curUnit_details.get('ects')
        curricular_unit.cu_readable_code = curUnit_details.get('curricularIUnitReadableCode', '')

        # Handle time format conversion
        hr_total_contacto = curUnit_details.get('hrTotalContacto', '00:00:00')
        try:
            hours, minutes = map(int, hr_total_contacto.split(':'))
            time_spent = time(hour=hours, minute=minutes)
        except ValueError:
            time_spent = time(hour=0, minute=0)

        curricular_unit.time_spent = time_spent

        try:
            cur_branch = Branch.objects.get(name=curUnit_details['curricularBranchName'])
        except Branch.DoesNotExist:
            cur_branch = Branch(name=curUnit_details['curricularBranchName'])
            cur_branch.save()

        curricular_unit.cu_branch = cur_branch
        curricular_unit.save()
