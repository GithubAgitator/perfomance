import httpx
from faker import Faker

faker = Faker()

body = {
  "email": faker.email(),
  "lastName": "Игорь",
  "firstName": "Бобров",
  "middleName": "Петрович",
  "phoneNumber": "12345"
}
creater_user = httpx.post("http://localhost:8003/api/v1/users", json=body)
print(creater_user.json())
print(creater_user.status_code)
ids = creater_user.json()['user']['id']
print(ids)


