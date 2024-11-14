import unittest
import requests
import json

class TestAPI(unittest.TestCase):
    """Integration tests for AI Chatbot and Predictive Analytics APIs."""

    AI_CHATBOT_API_URL = "http://localhost:8000"
    PREDICTIVE_ANALYTICS_API_URL = "http://localhost:8002"

    def test_ai_chatbot_endpoint(self):
        """Test AI Chatbot /chat endpoint."""
        payload = {
            "message": "Hello"
        }
        response = requests.post(f"{self.AI_CHATBOT_API_URL}/chat", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("response", data)
        self.assertEqual(data["response"], "Echo: Hello")

    def test_predictive_analytics_endpoint(self):
        """Test Predictive Analytics /risk_assessment endpoint."""
        payload = {
            "feature1": 1.0,
            "feature2": "A"
        }
        response = requests.post(f"{self.PREDICTIVE_ANALYTICS_API_URL}/risk_assessment", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("risk_score", data)
        self.assertEqual(data["risk_score"], 0.75)

if __name__ == '__main__':
    unittest.main()

