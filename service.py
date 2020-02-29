from models import AgendaModel

class AgendaService:
    def __init__(self):
        self.model = AgendaModel()
        
    def create(self, raw_json):
        return self.model.create(raw_json)