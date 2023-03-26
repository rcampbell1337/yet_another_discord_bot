class MockMongoClient:
    def __init__(self, connection_url: str):
        self.connection_url = connection_url
