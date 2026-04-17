import httpx
from user import ids

body = {
"userId": ids
}

response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=body)
print(response.json())
print(response.status_code)