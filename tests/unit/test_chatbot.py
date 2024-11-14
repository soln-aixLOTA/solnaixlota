import unittest
import json
from backend.python_service.src.app import app

class TestChatbot(unittest.TestCase):
    """Unit tests for the Flask Chatbot application."""

    def setUp(self):
        """Set up the test client."""
        self.client = app.test_client()

    def test_health_check(self):
        """Test the health check endpoint."""
        response = self.client.get('/healthz')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'OK')

    def test_readiness_check(self):
        """Test the readiness check endpoint."""
        response = self.client.get('/readyz')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'Ready')

    def test_metrics_endpoint(self):
        """Test the metrics endpoint."""
        response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/plain', response.content_type)

    def test_process_endpoint(self):
        """Test the process endpoint."""
        response = self.client.post(
            '/process',
            json={'message': 'Background Task'},
            headers={'X-API-Key': 'test_key'}
        )
        self.assertEqual(response.status_code, 202)
        data = json.loads(response.data)
        self.assertIn('task_id', data)
        self.assertEqual(data['status'], 'Processing')

if __name__ == '__main__':
    unittest.main() 