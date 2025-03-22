import requests
from tests.api.endpoints.base_endpoint import Endpoint
from tests.api.payload.payloads import headers


class Task(Endpoint):
    schema = {
  "title": "string",
  "description": "string",
  "completed": True
}

    def new_task(self, payload, session):
        self.response = session.post(f'{self.url}/api/tasks',
                                      json=payload, headers=headers)
        self.response_json = self.response.json()
        print("Response Status Code for task creation:", self.response.status_code)  # Debugging
        print("Response JSON:", self.response_json)  # Debugging

    def get_task_id(self):
        task_id = self.response_json.get('id')
        return task_id

    def get_task_details(self,session):
        task_id = self.get_task_id()
        self.response = session.get(f'{self.url}/api/tasks/{task_id}', headers=headers)
        self.response_json = self.response.json()


    def update_task(self, payload, session):
        task_id = self.get_task_id()
        self.response = session.put(f'{self.url}/api/tasks/{task_id}',
                                      json=payload, headers=headers)
        self.response_json = self.response.json()
        print("Response Status Code for task change:", self.response.status_code)  # Debugging
        print("Response JSON:", self.response_json)  # Debugging

    def update_status_task(self, session):
        task_id = self.get_task_id()
        self.response = session.post(f'{self.url}/api/tasks/{task_id}/toggle')
        self.response_json = self.response.json()
        print("Response Status Code for update of task status:", self.response.status_code)  # Debugging
        print("Response JSON:", self.response_json)  # Debugging

    def delete_task(self, session):
        task_id = self.get_task_id()
        assert task_id is not None, "Cannot delete task. Task ID is None!"

        self.response = session.delete(f'{self.url}/api/tasks/{task_id}')
        print(f"Delete Response Status Code: {self.response.status_code}")

        if self.response.status_code == 204:
            self.response_json = None  # No JSON response
            print("✅ Task deleted successfully (204 No Content)")
        else:
            try:
                self.response_json = self.response.json()
                print(f"Delete Response JSON: {self.response_json}")  # Debugging print
            except requests.exceptions.JSONDecodeError:
                print("No JSON response received from DELETE request")
                self.response_json = None  # Handle cases where no JSON is returned
