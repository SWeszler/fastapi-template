from fastapi.testclient import TestClient
from app.main import app
from app.modules.items import deps

client = TestClient(app)


class MockDB:

    def execute(self, sql):
        print(sql)
        return [{
            "id": 1,
            "title": "Unit Test 1",
            "description": "The first item from unit test.",
        }]


def mock_db():
    return MockDB()


app.dependency_overrides[deps.get_db] = mock_db


def test_get_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "title": "Unit Test 1",
        "description": "The first item from unit test.",
    }]
