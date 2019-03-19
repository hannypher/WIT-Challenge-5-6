from datetime import datetime
class  Entry():
    def __init__(self, entry_id, title, description, emotions):
        self.entry_id = entry_id
        self.title= title
        self.description = description
        self.emotions = emotions
        self.entry_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
