import logging
from requests import Response

class Requests:
    """Class representing a mock of the Python requests module.
    """
    def __init__(self, status_code: str = None, response_message: str = None):
        """Constructor method.

        Args:
            status_code (str, optional): The mocked response status code. Defaults to None.
            response_message (str, optional): The mocked response message. Defaults to None.
        """
        self.status_code = status_code
        self.response_message = response_message
        self.logger = logging.getLogger("logger")

    def get(self, url: str) -> Response:
        """Mocks a get request.

        Args:
            url (str): The url to send the request to.

        Returns:
            Response: The response object.
        """
        self.logger.Debug(f"Mocking a get request with URL: {url}")
        if self.status_code and self.response_message:
            return Response({"content": self.response_message}, self.status_code)
        return Response({"content": "success"}, 204)

    def post(self, url: str, json: str) -> Response:
        """Mocks a post request.

        Args:
            url (str): The url to send the request to.

        Returns:
            Response: The response object.
        """
        self.logger.debug(f"Mocking a post request with URL: {url} and json: {json}")
        if self.status_code and self.response_message:
            return Response({"content": self.response_message}, self.status_code)
        return Response({"content": "success"}, 204)

class Response:
    """Class representing a mock of a response object.
    """
    def __init__(self, json_data: str, status_code: str):
        """Constructor Method.

        Args:
            json_data (str): The JSON Data.
            status_code (str): The Status code.
        """
        self.json_data = json_data
        self.status_code = status_code

    def json(self) -> str:
        """Default method which may be used in response objects.

        Returns:
            str: Json data
        """
        return self.json_data
