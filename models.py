from pprint import pprint
import json

class AgendaModel:

    def __init__(self):
        self.sections = {}
        pass

    def create(self, raw_json):
        # transform raw json to agenda
        j = json.loads(raw_json)
        checklists = sorted(j['checklists'], key=lambda k: k.get('pos', 0), reverse=False)
        for checklist in checklists:
            if len(checklist['checkItems']) > 0:
                agenda_items = []
                for i in range(len(checklist['checkItems'])):
                    agenda_items.append(checklist['checkItems'][i]['name'])

                self.sections[checklist['name']] = agenda_items
        return self.sections
