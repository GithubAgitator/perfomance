from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum

class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"

class StatusType(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"

class CardPaymentSystem(StrEnum):
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"


class CardIssueVirtualSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    pin: str
    cvv: str
    type: CardType
    status: StatusType
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: CardPaymentSystem = Field(alias="paymentSystem")

class CreateCardsIssueVirtualResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    card: CardIssueVirtualSchema

class CardIssuePhysicalSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    pin: str
    cvv: str
    type: CardType
    status: StatusType
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: CardPaymentSystem = Field(alias="paymentSystem")

class CreateCardsIssuePhysicalResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    card: CardIssuePhysicalSchema

class CreateVirtualCardSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")

class CreatePhysicalCardSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")
