from typing import Dict, List


class Collection:
    data = []

    def __init__(self, collection_name: str, seed = None) -> None:
        self.collection_name = collection_name
        if seed:
            self.data.append(seed)

    def find(self) -> List[dict]:
        return self.data
    
    def insert_one(self, data: Dict[str, str]) -> None:
        self.data.append(data)

class Database:
    def __init__(self, db_name: str, seed = None) -> None:
        self.db_name = db_name
        self.collection = None
        self.seed = seed
    
    def get_collection(self, collection_name: str) -> Collection:
        if self.seed:
            return Collection(collection_name, self.seed)
        else:
            return Collection(collection_name)

class MockMongoClient:
    def __init__(self, connection_url: str, seed: list[dict] = None) -> None:
        self.connection_url = connection_url
        self.seed = seed

    def get_database(self, db_name: str) -> Database:
        if self.seed:
            return Database(db_name, self.seed)
        else:
            return Database(db_name)