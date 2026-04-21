import httpx
from httpx_create_debet_cards import debit_account_id, debit_cards_id


body = {
  "status": "COMPLETED",
  "amount": 1000,
  "cardId": debit_cards_id,
  "accountId": debit_account_id
}


response = httpx.post(f"http://localhost:8003/api/v1/operations/make-top-up-operation", json=body, timeout=60.0)
print(response.json())
print(response.status_code)
