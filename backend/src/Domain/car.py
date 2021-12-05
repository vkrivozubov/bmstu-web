from DTO.car import CarDTO

class CarDatabaseToDomainConverter:
    def __init__(self):
        ()

    def convert(self, tuple):
        return Car(
            tuple[0],
            tuple[1],
            tuple[2],
            tuple[3],
            tuple[4],
        )

class CarDomainToDTOConverter:
    def __init__(self):
        ()

    def convert(self, domain_model):
        return CarDTO(
            domain_model.id,
            domain_model.model,
            domain_model.cost,
            domain_model.is_available
        )

class Car:
    def __init__(self, id, model, cost, dealership_id, is_available):
        self.id = id
        self.model = model
        self.cost = cost
        self.dealership_id = dealership_id
        self.is_available = is_available
