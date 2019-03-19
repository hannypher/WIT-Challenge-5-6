from flask import jsonify, request
from flask.views import MethodView
from models import EntryDiaries
 
entry_object = EntryDiaries()

class EntryView(MethodView):

    def post(self, entry_id, post_data):      
        keys = ("title",  "description", "emotions")
        
        if not set(keys).issubset(set(request.json)):
            return jsonify({'Alert':'fill all fields'}) 
            
        
        if entry_id.exit_entry(request.json['title']):
                return jsonify({'Alert':'your entry has already been input'})
    
        post_data = request.get_json()
        title = request.json['title']
        description = request.json['description'] 
        emotions = request.json['emotions']
        id = 'id' 

        
        entry_id.add_entry(id, title, description, emotions)

        response_object =  entry_id.__dict__
        
        return jsonify(response_object), 201


    def get(self, entry_id=None):
        if entry_id is None:
            if entry_id.get_all_entries() is True:
                return jsonify({'entry':'No new entry,Please enter an entry'})
            return jsonify({'entry': entry_id.get_all_entries()}), 200
        return jsonify({'entry': entry_id.get_one_entry(entry_id)}), 200

    def put(self,entry_id):
        post_data = request.get_json()

        key= 'title'
        if key not in post_data:
            return jsonify({'alert':'input feilds'})
        
        return jsonify({'new title':entry_id.update(entry_id)}),200

