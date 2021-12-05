class CarDTO:
    def __init__(self, id, model, cost, is_available):
        self.id = id
        self.model = model
        self.cost = cost
        self.is_available = is_available

    def get_dict(self):
        return {
            'id': self.id,
            'model': self.model,
            'cost': self.cost,
            'is_available': self.is_available
        }