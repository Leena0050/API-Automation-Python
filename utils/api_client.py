import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint):
        """Make a GET request to the specified endpoint"""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response

    def post(self, endpoint, data):
        """Make a POST request to the specified endpoint with data"""
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        return response

    def put(self, endpoint, data):
        """Make a PUT request to the specified endpoint with data"""
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        return response

    def delete(self, endpoint):
        """Make a DELETE request to the specified endpoint"""
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        return response
