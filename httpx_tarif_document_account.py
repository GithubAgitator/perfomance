import httpx
from httpx_open_credit_cards_account import account_id


response = httpx.get(f"http://localhost:8003/api/v1/documents/tariff-document/{account_id}", timeout=60.0)
print(response.json())
print(response.status_code)
