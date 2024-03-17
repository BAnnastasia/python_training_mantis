from model.project import Project
import datetime


def test_add_project(app):
    project = Project(name="Test_new_create5 "+str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
    old_projects = app.soap.projects_get_user_accessible()
    app.project.create(project)
    new_projects = app.soap.projects_get_user_accessible()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)