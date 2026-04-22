import httpx
from httpx_make_purchare_operation import operation_id



response = httpx.get(f"http://localhost:8003/api/v1/operations/{operation_id}", timeout=60.0)
print(response.json())
print(response.status_code)

