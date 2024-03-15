from model.project import Project
import datetime

def test_add_project(app):
    project = Project(name="Test_new_create5 "+str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
    username = app.session.username
    password = app.session.password
    old_projects = app.soap.projects_get_user_accessible(username, password)
    app.project.create(project)
    new_projects = app.soap.projects_get_user_accessible(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)