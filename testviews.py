import unittest
import json
from run2 import APP

class TestViews(unittest.TestCase):
  

    def setUp(self):

        self.question = APP
        self.client = self.question.test_client
    
    def test_get_all_entries(self):

        result = self.client().get('/api/v1/entries/')
        self.assertEqual(result.status_code,200)
        
    def test_get_one_entry(self):

        result = self.client().get('/api/v1/entries/2')
        self.assertEqual(result.status_code,301)

    def test_add_entry(self):

        result = self.client().post('/api/v1/entries/', content_type="application/json", data=json.dumps(
            dict(title="life", description="what happened", emotions="happy", entry_id="1",)))
        self.assertEqual(result.status_code, 201)
        
    def test_update(self):
        
        result = self.client().post('/api/v1/entries/', content_type="application/json", data=json.dumps(
            dict(title="life2", description="about today", emotions="undecided")))
        result = self.client().put('/api/v1/entries/2/', content_type="application/json", data=json.dumps(dict(title='life')))      
        self.assertEqual(result.status_code, 200)