import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_and_get_transaction():
    # Add a transaction
    txn_data = {
        "user_id": "user_123",
        "amount": 150.75,
        "currency": "USD",
        "description": "Test transaction"
    }
    response = client.post("/transactions/", json=txn_data)
    assert response.status_code == 200
    created_transaction = response.json()
    assert created_transaction["user_id"] == txn_data["user_id"]
    assert created_transaction["amount"] == txn_data["amount"]
    assert created_transaction["description"] == txn_data["description"]
    assert "id" in created_transaction
    assert "timestamp" in created_transaction

    # Get transactions for the user
    response = client.get(f"/transactions/{txn_data['user_id']}")
    transactions = response.json()
    assert any(txn["amount"] == txn_data["amount"] for txn in transactions)