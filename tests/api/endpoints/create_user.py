import requests
from tests.api.endpoints.base_endpoint import Endpoint


class CreateUser(Endpoint):
    schema = {
  "username": "string",
  "password": "string"
}

    def new_user(self, payload):
        self.response = requests.post(f'{self.url}/api/register',
                                      json=payload)
        self.response_json = self.response.json()
        print("Response Status Code:", self.response.status_code)
        print("Response JSON:", self.response_json)

