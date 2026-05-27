from typing import List
from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum

class TypeOperations(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

class StatusOperations(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationDictSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class GetOperationResponseSchema(BaseModel):
    operations: List[OperationDictSchema]

class OperationsSummarySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    spent_amount: int = Field(alias="spentAmount")
    received_amount: int = Field(alias="receivedAmount")
    cashback_amount: int = Field(alias="cashbackAmount")

class GetOperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema

class OperationReceiptSchema(BaseModel):
    url: str
    document: str

class GetOperationReceiptResponseSchema(BaseModel):
    receipt: OperationReceiptSchema

class OperationsSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class GetOperationsResponseSchema(BaseModel):
    operation: OperationsSchema

class OperationsMakeFreeOperationSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class PostOperationsMakeFreeOperationResponseSchema(BaseModel):
    operation: OperationsMakeFreeOperationSchema

class OperationMakeTopUpSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class CreatedOperationMakeTopUpResponseSchema(BaseModel):
    operation: OperationMakeTopUpSchema

class OperationMakeCashbackSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class CreatedOperationMakeCashbackResponseSchema(BaseModel):
    operation: OperationMakeCashbackSchema

class OperationMakeTransferSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class CreatedOperationMakeTransferResponseSchema(BaseModel):
    operation: OperationMakeTransferSchema

class OperationMakePurchaseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class CreatedOperationMakePurchaseResponseSchema(BaseModel):
    operation: OperationMakePurchaseSchema


class CreatedMakeBillPaymentSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class CreatedCreatedMakeBillPaymentResponseSchema(BaseModel):
    operation: CreatedMakeBillPaymentSchema

class OperationMakeCashWithdrawalSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: TypeOperations
    status: StatusOperations
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class CreatedOperationMakeCashWithdrawalResponseSchema(BaseModel):
    operation: OperationMakeCashWithdrawalSchema


class GetOperationsQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class GetOperationsSummaryQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class GetOperationReceiptQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationsIdQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class StatusOperationsRequest(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class MakeFreeOperationRequestApiSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: StatusOperationsRequest
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTopUpOperationRequestApiSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: StatusOperationsRequest
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashbackOperationsRequestApiSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: StatusOperationsRequest
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTransferOperationRequestApiSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: StatusOperationsRequest
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakePurchaseOperationRequestApiSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: StatusOperationsRequest
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str

class MakeBillPaymentOperationApiSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: StatusOperationsRequest
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashWithdrawalOperationApiSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: StatusOperationsRequest
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
