from Domain.car import CarDatabaseToDomainConverter

class CarDatabaseModel:
    def __init__(self, tuple):
        self.id = tuple[0]
        self.model = tuple[1]
        self.cost = tuple[2]
        self.dealership_id = tuple[3]
        self.is_available = tuple[4]

class CarRepository:

    def __init__(self, conn):
        self.conn = conn

    def get_cars(self, dealership_id):
        cur = self.conn.cursor()
        cur.execute(f'SELECT * from cars WHERE dealership_id = {dealership_id}')
        cars = cur.fetchall()

        converter = CarDatabaseToDomainConverter()
        domain_cars = []

        for car in cars:
            domain_cars.append(converter.convert(car))

        return domain_cars

    def create_car(self, domain_car):
        model = domain_car.model
        cost = domain_car.cost
        dealership_id = domain_car.dealership_id
        is_available = domain_car.is_available

        cur = self.conn.cursor()

        try:
            cur.execute(f'INSERT INTO cars (model, cost, dealership_id, is_available) VALUES (\'{model}\', \'{cost}\', \'{dealership_id}\', \'{is_available}\');')
        except:
            self.conn.rollback()
            raise Exception('transaction failed')

        self.conn.commit()

    def delete_car(self, id):
        cur = self.conn.cursor()
        try:
            cur.execute(f'DELETE FROM cars WHERE id = {id}')
        except:
            self.conn.rollback()
            raise Exception('transaction failed')

        self.conn.commit()

    def rent_car(self, id):
        cur = self.conn.cursor()
        try:
            cur.execute(f'UPDATE cars SET is_available = true WHERE id = {id}')
        except:
            self.conn.rollback()
            raise Exception('transaction failed')

        self.conn.commit()

    def unrent_car(self, id):
        cur = self.conn.cursor()
        try:
            cur.execute(f'UPDATE cars SET is_available = false WHERE id = {id}')
        except:
            self.conn.rollback()
            raise Exception('transaction failed')

        self.conn.commit()