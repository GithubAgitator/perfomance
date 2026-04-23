import httpx
from faker import Faker

faker = Faker()
client = httpx.Client(
  base_url="http://localhost:8003",
  timeout=5,
  headers={"Autorization": "Bearer ///"}
)
body = {
  "email": faker.email(),
  "lastName": "Игорь",
  "firstName": "Бобров",
  "middleName": "Петрович",
  "phoneNumber": "12345"
}
creater_user = client.post("/api/v1/users", json=body)
print(creater_user.json())
print(creater_user.status_code)
print(creater_user.request.headers)
ids = creater_user.json()['user']['id']
print(ids)


