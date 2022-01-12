class UserDatabaseToDomainConverter:
    def __init__(self):
        ()
        
    def convert(self, database_model):
        return User(database_model.id, database_model.username, database_model.password, database_model.role)

class User:
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
