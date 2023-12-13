import unittest
import sys
import os
import json

# Add the server/src/directory to the path for importing
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'server', 'src'))

from main import app

class TestServer(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_receive_data(self):
        # Prepare the data and headers
        payload = json.dumps({'key': 'value'})
        headers = {'Content-Type': 'application/json'}

        # Use the client to send a POST request to the server
        response = self.client.post('/recieve_data', data=payload, headers=headers)
        
        # Check the response status code and data
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {'status': 'success'})

if __name__ == '__main__':
    unittest.main()