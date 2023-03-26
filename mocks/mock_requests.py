from requests import Response


class Requests:
    def get(url) -> Response:
        return Response({"content": "success"}, 200)
    
    def post(url) -> Response:
        return Response({"content": "success"}, 204)
    
    def patch(url) -> Response:
        return Response({"content": "success"}, 200)
    
    def delete(url) -> Response:
        return Response({"content": "success"}, 200)

class Response:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data