from DTO.dealership import DealershipDTO

class DealershipDatabaseToDomainConverter:
    def __init__(self):
        ()

    def convert(self, tuple):
        return Dealership(
            tuple[0],
            tuple[1],
            tuple[2],
            tuple[3],
        )

class DealershipDomainToDTOConverter:
    def __init__(self):
        ()

    def convert(self, domain_model):
        return DealershipDTO(
            domain_model.id,
            domain_model.name,
            domain_model.description,
            domain_model.owner_id
        )

class Dealership:
    def __init__(self, id, name, description, owner_id):
        self.id = id
        self.name = name
        self.description = description
        self.owner_id = owner_id
