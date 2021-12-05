from Domain.user import*

class UserDatabaseModel:
    def __init__(self, tuple):
        self.id = tuple[0]
        self.username = tuple[1]
        self.password = tuple[2]
        self.role = tuple[3]

class UserRepository:

    def __init__(self, conn):
        self.conn = conn

    def get_all_users(self):
        cur = self.conn.cursor()
        cur.execute('SELECT * from users;')
        users = cur.fetchall()

        converter = UserDatabaseToDomainConverter()
        users_domain = []

        for user in users:
            model = UserDatabaseModel(user)
            users_domain.append(converter.convert(model))

        return users_domain

    def add_new_user(self, user_domain):
        username = user_domain.username
        password = user_domain.password
        role = user_domain.role
        cur = self.conn.cursor()
        cur.execute(f'INSERT INTO users (username, password, role) VALUES (\'{username}\', \'{password}\', \'{role}\');')
        self.conn.commit()
