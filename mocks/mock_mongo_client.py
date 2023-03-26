class MockMongoClient:
    def __init__(self, connection_url: str, seed=None):
        self.connection_url = connection_url
