import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_character_id_required_json_empty(self):
        response = self.app.post('/character', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json )
        self.assertEqual(response.json['error'], 'Character ID is required')
    
    def test_character_id_required_query_empty(self):
        response = self.app.post('/character')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Character ID is required')

    def test_character_id_not_a_number(self):
        response = self.app.post('/character', json={'character_id': 'abc'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Character is not a number')

    def test_character_found(self):
        response = self.app.post('/character', json={'character_id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.json)
        self.assertIn('status', response.json)

    def test_character_not_found(self):
        response = self.app.post('/character', json={'character_id': 9999})
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Character not found')
    

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
