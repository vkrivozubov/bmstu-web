from car_repository import CarRepository
from dealership_repository import DealershipRepository
from user_repository import UserRepository
import psycopg2

class RepositoryFabrique:

    conn = None

    def __init__(self):
        conn = psycopg2.connect(
            host="localhost",
            database="rental",
            user="postgres",
            password="zVQ2zYTe"
        )

        self.conn = conn
    
    def create_user_repository(self):
        return UserRepository(self.conn)

    def create_dealership_repository(self):
        return DealershipRepository(self.conn)

    def create_car_repository(self):
        return CarRepository(self.conn)
