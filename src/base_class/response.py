from src.enums.global_emuns import GlobalErrorMassages


class Response():

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    # validate body of response PYDANTIC
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
                print(type(schema.parse_obj(item)))
        else:
            schema.parse_obj(self.response_json)
        return self

    # validate status code of response PYDANTIC
    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, self
        else:
            assert self.response_status_code == status_code, self
        return self

    def __str__(self):
        return (
            f'\n Status code: {self.response_status_code} \n'
            f'Requested URL: {self.response.url} \n'
            f'Response body: {self.response_json}'
        )
