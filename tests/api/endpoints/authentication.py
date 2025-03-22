from tests.api.endpoints.base_endpoint import Endpoint


class AuthenticateUser(Endpoint):
    schema = {
  "username": "string",
  "password": "string"
}


    def login_user(self, payload, session):
        self.response = session.post(f'{self.url}/api/login',
                                      json=payload)
        self.response_json = self.response.json()
        print("Response Status Code:", self.response.status_code)  # Debugging
        print("Response JSON:", self.response_json)  # Debugging
        return session