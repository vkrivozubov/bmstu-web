class UserDatabaseToDomainConverter:
    def __init__(self):
        ()
        
    def convert(self, database_model):
        return User(database_model.username, database_model.password, database_model.role)

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
