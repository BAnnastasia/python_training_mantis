from pony.orm import *
from model.project import Project

class ORMFixture:
    db = Database()

    class ORMProject (db.Entity):
        _table_= 'mantis_project_table'
        id = PrimaryKey(int, column='id')
        name = Optional(str, column='name')


    def __init__(self,host,name,user, password):
        self.db.bind(provider='mysql', host=host, user=user, passwd=password, db=name)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_project_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), name=project.name)
        return list(map(convert,projects))

    @db_session
    def get_project_list(self):
        return self.convert_project_to_model(select(g for g in ORMFixture.ORMProject))