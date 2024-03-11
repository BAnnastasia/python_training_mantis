from model.project import Project
import datetime

def test_add_project(app, orm):
    project = Project(name="Test_new_create5 "+str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
    app.session.login("administrator", "root")
    old_projects = orm.get_project_list()
    app.project.create(project)
    new_projects = orm.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)