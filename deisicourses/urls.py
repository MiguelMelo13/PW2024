from django.urls import path
from . import views

app_name = 'deisicourses'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('courses/', views.courses_view, name='courses'),
    path('curricularUnits/', views.curUnits_view, name='curricularUnits'),
    path('projects/', views.projects_view, name='projects'),



    path('project/<int:project_id>/', views.project_detail_view, name='project_detail'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('curricularUnit/<int:curUnit_id>/', views.curUnit_detail_view, name='curUnit_detail'),
    
]
