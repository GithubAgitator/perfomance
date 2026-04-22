import httpx
from httpx_open_credit_cards_account import account_id, credit_cards_id


body = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": credit_cards_id,
  "accountId": account_id,
  "category": "taxi"
}

response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=body, timeout=60.0)
print(response.json())
print(response.status_code)
operation_id = response.json()["operation"]["id"]
print(operation_id)
