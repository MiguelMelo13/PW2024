from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    author = models.CharField(max_length=50)
    video_link = models.URLField(max_length=250, blank=True, null=True)
    git_repo_link = models.URLField(max_length=250, blank=True, null=True)
    programming_languages = models.ManyToManyField('Programming_Language')
    curricular_unit = models.ForeignKey('CurricularUnit', on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name



class Programming_Language(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=75)
    curricular_units = models.ManyToManyField('CurricularUnit')

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=150)
    presentation = models.TextField()
    objectives = models.TextField()
    competences = models.TextField()
    scientific_area = models.CharField(max_length=50)
    director = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    deliberation = models.URLField(max_length=250, blank=True, null=True)
    career_opportunities = models.TextField()
    curricular_units = models.ManyToManyField('CurricularUnit')

    def __str__(self):
        return self.name

    
    
class CurricularUnit(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    semester = models.CharField(max_length=15)
    ects = models.IntegerField()
    cu_readable_code = models.CharField(max_length=50)
    time_spent = models.TimeField()
    cu_branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    programming_languages = models.ManyToManyField('Programming_Language')
    teachers = models.ManyToManyField('Teacher')
    def __str__(self):
        return self.name
