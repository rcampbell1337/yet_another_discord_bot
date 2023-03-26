from typing import Dict
from requests import Response


class Requests:
    def get(self, url) -> Response:
        return Response({"content": "success"}, 200)
    
    def post(self, url: str, json) -> Response:
        return Response({"content": "success"}, 204)
    
    def patch(self, url) -> Response:
        return Response({"content": "success"}, 200)
    
    def delete(self, url) -> Response:
        return Response({"content": "success"}, 200)

class Response:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data