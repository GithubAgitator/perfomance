from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.geteway.client import build_gateway_http_client
from clients.http.geteway.operations.schema import GetOperationResponseSchema, GetOperationsQuerySchema, \
    GetOperationsSummaryResponseSchema, GetOperationsSummaryQuerySchema, GetOperationReceiptResponseSchema, \
    GetOperationsResponseSchema, MakeFreeOperationRequestApiSchema, PostOperationsMakeFreeOperationResponseSchema, \
    MakeTopUpOperationRequestApiSchema, CreatedOperationMakeTopUpResponseSchema, \
    CreatedOperationMakeCashbackResponseSchema, MakeCashbackOperationsRequestApiSchema, \
    MakeTransferOperationRequestApiSchema, CreatedOperationMakeTransferResponseSchema, \
    CreatedOperationMakePurchaseResponseSchema, MakePurchaseOperationRequestApiSchema, \
    MakeBillPaymentOperationApiSchema, CreatedCreatedMakeBillPaymentResponseSchema, \
    CreatedOperationMakeCashWithdrawalResponseSchema, MakeCashWithdrawalOperationApiSchema


class OperationsGatewayHTTPClient(HTTPClient):
    """Получение информации об операции по operation_id"""
    def get_operation_api(self, query: GetOperationsQuerySchema) -> Response:
        return self.get(f"/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operation(self, account_id: str) -> GetOperationResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operation_api(query=query)
        return GetOperationResponseSchema.model_validate_json(response.text)

    """Получение чека по операции"""
    def get_operation_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        return self.get(f"/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operation_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operation_summary_api(query=query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)


    """Получение списка операций для определенного счета"""
    def get_operations_receipt_api(self, operation_id: str) -> Response:
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operations_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    """Получение статистики по операциям для определенного счета"""
    def get_operations_api(self, operation_id: str) -> Response:
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operations(self, operation_id: str) -> GetOperationsResponseSchema:
        response = self.get_operations_api(operation_id)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    """Создание операции комиссии"""
    def make_fee_operation_api(self, request: MakeFreeOperationRequestApiSchema) -> Response:
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_fee_operation(self, card_id: str, account_id: str) -> PostOperationsMakeFreeOperationResponseSchema:
        request = MakeFreeOperationRequestApiSchema(
            status="COMPLETED",
            amount=10,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return PostOperationsMakeFreeOperationResponseSchema.model_validate_json(response.text)

    """Создание операции пополнения"""
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestApiSchema) -> Response:
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation(self, card_id: str, account_id: str) -> CreatedOperationMakeTopUpResponseSchema:
        request = MakeTopUpOperationRequestApiSchema(
            status="COMPLETED",
            amount=10,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return CreatedOperationMakeTopUpResponseSchema.model_validate_json(response.text)

    """Создание операции кэшбэка"""
    def make_cashback_operation_api(self, request: MakeCashbackOperationsRequestApiSchema) -> Response:
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation(self, card_id: str, account_id: str) -> CreatedOperationMakeCashbackResponseSchema:
        request = MakeCashbackOperationsRequestApiSchema(
            status="COMPLETED",
            amount=10,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return CreatedOperationMakeCashbackResponseSchema.model_validate_json(response.text)

    """Создание операции перевода"""
    def make_transfer_operation_api(self, request: MakeTransferOperationRequestApiSchema) -> Response:
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation(self, card_id: str, account_id: str) -> CreatedOperationMakeTransferResponseSchema:
        request = MakeTransferOperationRequestApiSchema(
            status="COMPLETED",
            amount=10,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return CreatedOperationMakeTransferResponseSchema.model_validate_json(response.text)

    """Создание операции покупки"""
    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestApiSchema) -> Response:
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation(self, card_id: str, account_id: str) -> CreatedOperationMakePurchaseResponseSchema:
        request = MakePurchaseOperationRequestApiSchema(
            status="COMPLETED",
            amount=10,
            card_id=card_id,
            account_id=account_id,
            category="R"
        )
        response = self.make_purchase_operation_api(request)
        return CreatedOperationMakePurchaseResponseSchema.model_validate_json(response.text)

    """Создание операции оплаты по счету"""
    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationApiSchema) -> Response:
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> CreatedCreatedMakeBillPaymentResponseSchema:
        request = MakeBillPaymentOperationApiSchema(
            status="COMPLETED",
            amount=10,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return CreatedCreatedMakeBillPaymentResponseSchema.model_validate_json(response.text)

    """Создание операции снятия наличных денег"""
    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationApiSchema) -> Response:
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> CreatedOperationMakeCashWithdrawalResponseSchema:
        request = MakeCashWithdrawalOperationApiSchema(
            status="COMPLETED",
            amount=10,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return CreatedOperationMakeCashWithdrawalResponseSchema.model_validate_json(response.text)

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
