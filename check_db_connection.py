from fixture.orm import ORMFixture
from model.project import Project

db = ORMFixture(host="127.0.0.1", name="bugtracker", user="root", password="")
try:
    l = db.get_project_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #connection.close()