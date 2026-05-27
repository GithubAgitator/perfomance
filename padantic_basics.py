from datetime import date
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel
import uuid


class CardsSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: date = Field(alias="expiryDate")
    payment_system: str = Field(alias="paymentSystem")

class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "CREDIT_CARD"
    cards: list[CardsSchema] = Field(default_factory=list)
    status: str = "ACTIVE"
    balance: float = 10.0


# Инициализируем модель AccountSchema через передачу аргументов
account_default_model = AccountSchema(
    id="card_id",
    type="CREDIT_CARD",
    # Добавили инициализацию списка вложенных моделей CardSchema
    cards=[
        CardsSchema(
            id="card-id",
            pin="1234",
            cvv="123",
            type="PHYSICAL",
            status="ACTIVE",
            accountId="account-id",
            cardNumber="1234123412341234",
            cardHolder="Alise Smith",
            expiryDate=date(2027, 3, 25),
            paymentSystem="VISA"
        )
    ],
    status="ACTIVE",
    balance=100.57,
)
account_dict = {
    "id": "card_id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alise Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11,
}

print('Account default model:', account_default_model)
account_model_dict = AccountSchema(**account_dict)
print(account_model_dict.model_dump(by_alias=True))