from entry import Entry
from flask import request


class EntryDiaries():
    def __init__(self):
        self.entries=[]

    def add_entry(self, entry_id, title, description, emotions):
        entry_list = [entry_id for entry_id in self.entries]

        id = len(entry_list) + 1
        entry = {
            'title': title, 
            'id':id,
            'description': description,
            'emotions' : emotions
             
        }
        self.entries.append(entry)
        return {'New entry': [
            entry for entry in self.entries]}  

    def get_all_daries(self):
        if not self.entries:
            return "No entry found"
        entry_dict = [entry.__dict__ for entry in self.entries]
        return entry_dict

    def get_one_entry(self, entry_id):
        available_entry_id = [
            entry for entry in self.entries
            if entry ['id'] == entry_id]
        if not available_entry_id:
            return {entry_id:"entry_id doesnot exist"}
        return available_entry_id

    def update(self,entry_id):
        for entry in self.entries:
            if entry_id == entry['id']:
                entry_json = request.get_json()
                title = entry_json['title']
                entry['title'] = title
                return {entry_id:'Event has been updated'}  

    def exit_entry(self, title):
        for entry in self.entries:
            if title == entry['title']:
                return True
        return False
