from enum import StrEnum
from typing import List
from pydantic import BaseModel, Field, ConfigDict

class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"

class CardStatus(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"

class CardSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: str = Field(alias="paymentSystem")

class TypeAccount(StrEnum):
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"

class AccountStatus(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    ACTIVE = "ACTIVE"
    PENDING_CLOSURE = "PENDING_CLOSURE"
    CLOSED = "CLOSED"

class AccountSchema(BaseModel):
    id: str
    type: TypeAccount
    cards: List[CardSchema]
    status: AccountStatus
    balance: float

class GetAccountResponseSchema(BaseModel):
    accounts: List[AccountSchema]

class CreateOpenDepositAccountResponseSchema(BaseModel):
    account: AccountSchema

class CreateOpenSavingsAccountResponseSchema(BaseModel):
    account: AccountSchema
class CreateOpenDebitAccountResponseSchema(BaseModel):
    account: AccountSchema
class CreateOpenCreditAccountResponseSchema(BaseModel):
    account: AccountSchema


class GetAccountQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")


class OpenDepositAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")


class OpenSavingsAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")


class OpenDebitCardAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")


class OpenCreditCardAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")