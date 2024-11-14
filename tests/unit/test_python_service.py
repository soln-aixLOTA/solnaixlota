import unittest
from src.app import app

class TestPythonService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_process_data(self):
        response = self.app.post('/process', json={"message": "Hello"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'success')

if __name__ == '__main__':
    unittest.main() 