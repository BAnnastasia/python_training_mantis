from model.project import Project
import random
import datetime
def test_delete_project(app,orm):
    if len(orm.get_project_list()) == 0:
        app.project.create(Project(name="test_name_delete"+str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))))
    old_projects = orm.get_project_list()
    project = random.choice(old_projects)

    app.project.delete_project_by_id(project.id) #

    new_project = orm.get_project_list()
    assert len(old_projects) - 1 == len(new_project)
    old_projects.remove(project)
    assert old_projects == new_project
