class DealershipDTO:
    def __init__(self, id, name, description, owner_id):
        self.id = id
        self.name = name
        self.description = description
        self.owner_id = owner_id

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner_id': self.owner_id
        }