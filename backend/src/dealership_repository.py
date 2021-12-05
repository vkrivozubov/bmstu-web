from Domain.dealership import*

class DealershipDatabaseModel:
    def __init__(self, tuple):
        self.id = tuple[0]
        self.name = tuple[1]
        self.description = tuple[2]
        self.owner_id = tuple[3]

class DealershipRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_dealerships(self):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM dealerships;')
        dealerships = cur.fetchall()

        domain_dealeships = []
        converter = DealershipDatabaseToDomainConverter()

        for dealer in dealerships:
            domain_dealeships.append(converter.convert(dealer))

        return domain_dealeships

    def create_dealership(self, domain_model):
        name = domain_model.name
        description = domain_model.description
        owner_id = domain_model.owner_id
        cur = self.conn.cursor()
        try:
            cur.execute(f'INSERT INTO dealerships (name, description, owner_id) VALUES (\'{name}\', \'{description}\', \'{owner_id}\');')
        except:
            self.conn.rollback()
            raise Exception('transaction failed')

        self.conn.commit()

    def remove_dealership(self, id):
        cur = self.conn.cursor()
        cur.execute(f'DELETE FROM dealerships WHERE id = {id}')
        self.conn.commit()