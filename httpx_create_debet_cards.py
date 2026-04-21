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


body2 = {
    "userId": creater_user.json()["user"]["id"]
}

creater_debit_cards = httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account", json=body2,
                                 timeout=60.0)
print(creater_debit_cards.json())
print(creater_debit_cards.status_code)
debit_account_id = creater_debit_cards.json()["account"]["id"]
debit_cards_id = creater_debit_cards.json()["account"]["cards"][0]["id"]
print(debit_cards_id)

body3 = {
    "userId": creater_user.json()["user"]["id"],
    "accountId": creater_debit_cards.json()["account"]["id"]
}

creater_issue_virtyal_cards = httpx.post("http://localhost:8003/api/v1/cards/issue-virtual-card", json=body3,
                                 timeout=60.0)
print(creater_issue_virtyal_cards.json())
print(creater_issue_virtyal_cards.status_code)



