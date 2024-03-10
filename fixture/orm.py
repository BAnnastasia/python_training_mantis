from pony.orm import *


class ORMFixture:
    db = Database()

    def __init__(self,host,name,user, password):
        self.db.bind(provider='mysql', host=host, user=user, passwd=password, db=name)
        self.db.generate_mapping()
        sql_debug(True)

