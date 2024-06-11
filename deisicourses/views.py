from django.shortcuts import render, get_object_or_404
from .models import Course, Project, Teacher, Branch, CurricularUnit, Programming_Language


def index_view(request):
    courses = Course.objects.all()
    projects = Project.objects.all()

    context = {
        'courses': courses,
        'projects': projects
    }

    return render(request, "deisicourses/index.html", context)

def courses_view(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, "deisicourses/courses.html", context)

def curUnits_view(request):
    curUnits = CurricularUnit.objects.all().order_by('year', 'semester', 'name')

    cu_years = {1: [], 2: [], 3: []}
    for cu in curUnits:
        cu_years[cu.year].append(cu)

    context = {
        'cu_years': cu_years
    }
    return render(request, "deisicourses/curricularUnits.html", context)

def projects_view(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }
    return render(request, "deisicourses/projects.html", context)

def project_detail_view(request,project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        'project' : project
    }

    return render(request, 'deisicourses/project.html', context )



def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    courseCUs = course.curricular_units.order_by('year', 'semester', 'name')

    cu_years = {1: [], 2: [], 3: []}
    for cu in courseCUs:
        cu_years[cu.year].append(cu)

    context = {
        'course': course,
        'cu_years': cu_years
    }

    return render(request, "deisicourses/course.html", context)

def curUnit_detail_view(request, curUnit_id):
    curUnit = get_object_or_404(CurricularUnit, id=curUnit_id)

    context = {
        'curUnit': curUnit
    }

    return render(request, "deisicourses/curUnit.html", context)
