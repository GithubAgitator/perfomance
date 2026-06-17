import grpc
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationRequest, MakeFeeOperationResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationRequest, MakeTopUpOperationResponse
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationRequest, MakeCashbackOperationResponse
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationRequest, MakeTransferOperationResponse
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import MakePurchaseOperationRequest, MakePurchaseOperationResponse
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import MakeBillPaymentOperationRequest, MakeBillPaymentOperationResponse
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import MakeCashWithdrawalOperationRequest, MakeCashWithdrawalOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryRequest, GetOperationsSummaryResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptRequest, GetOperationReceiptResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.operations.operation_pb2 import OperationStatus
from grpcio_creater_cards import get_cards_physical_request_id
from grpcio_get_account import id_deposit_account, id_credit_account, debit_account_id
from tools.fakers import fake

channel = grpc.insecure_channel("localhost:9003")


operations_gateway_service = OperationsGatewayServiceStub(channel)

create_make_free_operation_request = MakeFeeOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=get_cards_physical_request_id,
    account_id=id_credit_account

)

# Отправляем запрос и получаем ответ
create_make_free_operation_response: MakeFeeOperationResponse = operations_gateway_service.MakeFeeOperation(create_make_free_operation_request)
print('Create make free operation response:', create_make_free_operation_response)


create_make_to_up_operation_request = MakeTopUpOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=get_cards_physical_request_id,
    account_id=id_deposit_account

)

# Отправляем запрос и получаем ответ
create_make_to_up_operation_response: MakeTopUpOperationResponse = operations_gateway_service.MakeFeeOperation(create_make_to_up_operation_request)
print('Create make to up operation response:', create_make_to_up_operation_response)
make_to_up_operation_id = create_make_to_up_operation_response.operation.id


create_make_cashback_operation_request = MakeCashbackOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=get_cards_physical_request_id,
    account_id=id_deposit_account

)

# Отправляем запрос и получаем ответ
create_make_cashback_operation_response: MakeCashbackOperationResponse = operations_gateway_service.MakeCashbackOperation(create_make_cashback_operation_request)
print('Create make cashback operation response:', create_make_cashback_operation_response)

create_make_transfer_operation_request = MakeTransferOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=get_cards_physical_request_id,
    account_id=id_deposit_account

)

# Отправляем запрос и получаем ответ
create_make_transfer_operation_response: MakeTransferOperationResponse = operations_gateway_service.MakeTransferOperation(create_make_transfer_operation_request)
print('Create make transfer operation response:', create_make_transfer_operation_response)


create_make_purchase_operation_request = MakePurchaseOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=get_cards_physical_request_id,
    account_id=id_deposit_account,
    category=fake.category()

)

# Отправляем запрос и получаем ответ
create_make_purchase_operation_response: MakePurchaseOperationResponse = operations_gateway_service.MakePurchaseOperation(create_make_purchase_operation_request)
print('Create make purchase operation response:', create_make_purchase_operation_response)

create_make_purchase_operation_request_debit = MakePurchaseOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=get_cards_physical_request_id,
    account_id=debit_account_id,
    category=fake.category()

)

# Отправляем запрос и получаем ответ
create_make_purchase_operation_response_debit: MakePurchaseOperationResponse = operations_gateway_service.MakePurchaseOperation(create_make_purchase_operation_request_debit)
print('Create make purchase operation response debit:', create_make_purchase_operation_response_debit)



create_make_bill_operation_request = MakeBillPaymentOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=get_cards_physical_request_id,
    account_id=id_deposit_account

)

# Отправляем запрос и получаем ответ
create_make_bill_operation_response: MakeBillPaymentOperationResponse = operations_gateway_service.MakeBillPaymentOperation(create_make_bill_operation_request)
print('Create make bill operation response:', create_make_bill_operation_response)
operation_bill_id = create_make_bill_operation_response.operation.id

create_make_cash_withdrawal_operation_request = MakeCashWithdrawalOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=get_cards_physical_request_id,
    account_id=id_deposit_account

)

# Отправляем запрос и получаем ответ
create_make_cash_withdrawal_operation_response: MakeCashWithdrawalOperationResponse = operations_gateway_service.MakeCashWithdrawalOperation(create_make_cash_withdrawal_operation_request)
print('Create make cash_withdrawal operation response:', create_make_cash_withdrawal_operation_response)


get_operations = GetOperationsRequest(account_id=str(id_deposit_account))
get_operations_response: GetOperationsResponse = operations_gateway_service.GetOperations(get_operations)
print('Get operations response:', get_operations)


get_operations_summary = GetOperationsSummaryRequest(account_id=str(id_deposit_account))
get_operations_summary_response: GetOperationsSummaryResponse = operations_gateway_service.GetOperationsSummary(get_operations_summary)
print('Get operations summary response:', get_operations_summary_response)


get_operations_receipt_request = GetOperationReceiptRequest(operation_id=operation_bill_id)
get_operations_receipt_response: GetOperationReceiptResponse = operations_gateway_service.GetOperationReceipt(get_operations_receipt_request)
print('Get operations receipt response:', get_operations_receipt_response)

get_operations_receipt_request_2 = GetOperationReceiptRequest(operation_id=make_to_up_operation_id)
get_operations_receipt_response_2: GetOperationReceiptResponse = operations_gateway_service.GetOperationReceipt(get_operations_receipt_request_2)
print('Get operations receipt response 2:', get_operations_receipt_response_2)

get_operation_id_request = GetOperationReceiptRequest(operation_id=operation_bill_id)
get_operations_id_response: GetOperationResponse = operations_gateway_service.GetOperation(get_operation_id_request)
print('Get operations id response:', get_operations_id_response)








