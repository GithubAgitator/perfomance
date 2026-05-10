from httpx import Response, QueryParams
from typing import TypedDict, List
from clients.http.client import HTTPClient
from clients.http.geteway.client import build_gateway_http_client



class OperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class GetOperationResponseDict(TypedDict):
    operations: List[OperationDict]

class OperationsSummary(TypedDict):
    spentAmount: int
    receivedAmount: int
    cashbackAmount: int

class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummary

class OperationReceipt(TypedDict):
    url: str
    document: str

class GetOperationReceiptResponseDict(TypedDict):
    receipt: OperationReceipt

class Operations(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class GetOperationsResponseDict(TypedDict):
    operation: Operations

class OperationsMakeFreeOperation(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class PostOperationsMakeFreeOperationResponseDict(TypedDict):
    operation: OperationsMakeFreeOperation

class OperationMakeTopUp(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class CreatedOperationMakeTopUpResponseDict(TypedDict):
    operation: OperationMakeTopUp

class OperationMakeCashback(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class CreatedOperationMakeCashbackResponseDict(TypedDict):
    operation: OperationMakeCashback

class OperationMakeTransfer(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class CreatedOperationMakeTransferResponseDict(TypedDict):
    operation: OperationMakeTransfer

class OperationMakePurchase(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class CreatedOperationMakePurchaseResponseDict(TypedDict):
    operation: OperationMakePurchase


class CreatedMakeBillPayment(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class CreatedCreatedMakeBillPaymentResponseDict(TypedDict):
    operation: CreatedMakeBillPayment

class OperationMakeCashWithdrawal(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str

class CreatedOperationMakeCashWithdrawalResponseDict(TypedDict):
    operation: OperationMakeCashWithdrawal


class GetOperationsQueryDict(TypedDict):
    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):
    accountId: str

class GetOperationReceiptQueryDict(TypedDict):
    operation_id: str


class GetOperationsIdQueryDict(TypedDict):
    operation_id: str

class MakeFreeOperationRequestApi(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationRequestApi(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationsRequestApi(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationRequestApi(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestApi(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str

class MakeBillPaymentOperationApi(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationApi(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class OperationsGatewayHTTPClient(HTTPClient):
    """Получение информации об операции по operation_id"""
    def get_operation_api(self, query: GetOperationsQueryDict) -> Response:
        return self.get(f"/api/v1/operations", params=QueryParams(**query))

    def get_operation(self, accountId: str) -> GetOperationResponseDict:
        query: GetOperationsQueryDict = {"accountId": accountId}
        response = self.get_operation_api(query=query)
        return response.json()

    """Получение чека по операции"""
    def get_operation_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        return self.get(f"/api/v1/operations/operations-summary", params=QueryParams(**query))

    def get_operation_summary(self, accountId: str) -> GetOperationsSummaryResponseDict:
        query: GetOperationsSummaryQueryDict = {"accountId": accountId}
        response = self.get_operation_summary_api(query=query)
        return response.json()


    """Получение списка операций для определенного счета"""
    def get_operations_receipt_api(self, operation_id: str) -> Response:
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operations_receipt_api(operation_id)
        return response.json()

    """Получение статистики по операциям для определенного счета"""
    def get_operations_api(self, operation_id: str) -> Response:
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operations(self, operation_id: str) -> GetOperationsResponseDict:
        response = self.get_operations_api(operation_id)
        return response.json()

    """Создание операции комиссии"""
    def make_fee_operation_api(self, request: MakeFreeOperationRequestApi) -> Response:
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_fee_operation(self, cardId: str, accountId: str) -> PostOperationsMakeFreeOperationResponseDict:
        request = MakeFreeOperationRequestApi(
            status="COMPLETED",
            amount=10,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    """Создание операции пополнения"""
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestApi) -> Response:
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_top_up_operation(self, cardId: str, accountId: str) -> CreatedOperationMakeTopUpResponseDict:
        request = MakeTopUpOperationRequestApi(
            status="COMPLETED",
            amount=10,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    """Создание операции кэшбэка"""
    def make_cashback_operation_api(self, request: MakeCashbackOperationsRequestApi) -> Response:
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_cashback_operation(self, cardId: str, accountId: str) -> CreatedOperationMakeCashbackResponseDict:
        request = MakeCashbackOperationsRequestApi (
            status="COMPLETED",
            amount=10,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    """Создание операции перевода"""
    def make_transfer_operation_api(self, request: MakeTransferOperationRequestApi) -> Response:
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_transfer_operation(self, cardId: str, accountId: str) -> CreatedOperationMakeTransferResponseDict:
        request = MakeTransferOperationRequestApi (
            status="COMPLETED",
            amount=10,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    """Создание операции покупки"""
    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestApi) -> Response:
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_purchase_operation(self, cardId: str, accountId: str) -> CreatedOperationMakePurchaseResponseDict:
        request = MakePurchaseOperationRequestApi(
            status="COMPLETED",
            amount=10,
            cardId=cardId,
            accountId=accountId,
            category="R"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    """Создание операции оплаты по счету"""
    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationApi) -> Response:
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_bill_payment_operation(self, cardId: str, accountId: str) -> CreatedOperationMakePurchaseResponseDict:
        request = MakeBillPaymentOperationApi(
            status="COMPLETED",
            amount=10,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    """Создание операции снятия наличных денег"""
    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationApi) -> Response:
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def make_cash_withdrawal_operation(self, cardId: str, accountId: str) -> CreatedOperationMakeCashWithdrawalResponseDict:
        request = MakeCashWithdrawalOperationApi(
            status="COMPLETED",
            amount=10,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
