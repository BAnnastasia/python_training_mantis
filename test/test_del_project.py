from model.project import Project
import random
import datetime
def test_delete_project(app):
    username = app.session.username
    password = app.session.password
    if len(app.soap.projects_get_user_accessible(username, password)) == 0:
        app.project.create(Project(name="test_name_delete"+str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))))
    old_projects = app.soap.projects_get_user_accessible(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_project = app.soap.projects_get_user_accessible(username, password)
    assert len(old_projects) - 1 == len(new_project)
    old_projects.remove(project)
    assert old_projects == new_project
