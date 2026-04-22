import httpx
from user import ids


body = {
    "userId": ids
}

response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=body, timeout=60.0)
print(response.json())
print(response.status_code)
account_id = response.json()["account"]["id"]
credit_cards_id = response.json()["account"]["cards"][0]["id"]
print(account_id)
print(credit_cards_id)