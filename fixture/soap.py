from suds.client import Client
from suds import WebFault
from model.project import Project
class SoapHelper:
    def __init__(self,app):
        self.app = app

    def can_login(self, username,password):
        client = Client(self.app.config['soap']['baseUrl_mantis'])
        try:
            client.service.mc_login(username,password)
            return True
        except WebFault:
            return False

    def projects_get_user_accessible(self):
        client = Client(self.app.config['soap']['baseUrl_mantis'])
        projects = client.service.mc_projects_get_user_accessible(self.app.session.username, self.app.session.password)
        return self.convert_project_to_model(projects)

    def convert_project_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), name=project.name)
        return list(map(convert, projects))






