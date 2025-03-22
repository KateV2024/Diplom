import jsonschema
import tests.api.settings


class Endpoint:
    response = None
    response_json = None
    schema = {}
    url = tests.api.settings.url

    def check_response_is_201(self):
        assert self.response.status_code == 201,\
            f'Expected 201, got {self.response.status_code}'

    def check_response_is_200(self):
        assert self.response.status_code == 200,\
            f'Expected 200, got {self.response.status_code}'

    def check_response_is_204(self):
        assert self.response.status_code == 204,\
            f'Expected 204, got {self.response.status_code}'

    def check_response_is_401(self):
        assert self.response.status_code == 401,\
            f'Expected 401, got {self.response.status_code}'

    def check_response_is_400(self):
        assert self.response.status_code == 400,\
            f'Expected 400, got {self.response.status_code}'

    def check_response_is_404(self):
        assert self.response.status_code == 404,\
            f'Expected 404, got {self.response.status_code}'

    def validate(self, data):
        jsonschema.validate(instance=data, schema=self.schema)

    def get_data(self):
        return self.response_json