from tests.api.endpoints.base_endpoint import Endpoint


class GetTasks(Endpoint):
    schema =  {
    "id": 0,
    "title": "string",
    "description": "string",
    "created_at": "2025-03-15T12:44:12.724Z",
    "completed": True,
    "user_id": 0
  }

    def get_tasks(self, session):
        self.response = session.get(f'{self.url}/api/tasks')
        self.response_json = self.response.json()
        print("Response Status Code:", self.response.status_code)  # Debugging
        print("Response JSON:", self.response_json)  # Debugging

