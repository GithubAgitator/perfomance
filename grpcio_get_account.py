import grpc
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import GetAccountsRequest, GetAccountsResponse
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, OpenDebitCardAccountResponse
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import OpenDepositAccountRequest, OpenDepositAccountResponse
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import OpenSavingsAccountRequest, OpenSavingsAccountResponse
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import OpenCreditCardAccountRequest, OpenCreditCardAccountResponse
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from grpcio_get_user import create_user_response_id

channel = grpc.insecure_channel("localhost:9003")


accounts_gateway_service = AccountsGatewayServiceStub(channel)

create_debit_accounts_request = OpenDebitCardAccountRequest(
    user_id=create_user_response_id
)

# Отправляем запрос и получаем ответ
create_debit_accounts_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(create_debit_accounts_request)
print('Create debit account response:', create_debit_accounts_response)
debit_account_id = create_debit_accounts_response.account.id


create_deposit_accounts_request = OpenDepositAccountRequest(
    user_id=create_user_response_id
)

# Отправляем запрос и получаем ответ
create_deposit_accounts_response: OpenDepositAccountResponse = accounts_gateway_service.OpenDepositAccount(create_deposit_accounts_request)
print('Create deposit account response:', create_deposit_accounts_response)
id_deposit_account = create_deposit_accounts_response.account.id

create_savings_accounts_request = OpenSavingsAccountRequest(
    user_id=create_user_response_id
)

# Отправляем запрос и получаем ответ
create_savings_accounts_response: OpenSavingsAccountResponse = accounts_gateway_service.OpenSavingsAccount(create_savings_accounts_request)
print('Create savings account response:', create_savings_accounts_response)



create_credit_accounts_request = OpenCreditCardAccountRequest(
    user_id=create_user_response_id
)

# Отправляем запрос и получаем ответ
create_credit_accounts_response: OpenCreditCardAccountResponse = accounts_gateway_service.OpenCreditCardAccount(create_credit_accounts_request)
print('Create credit account response:', create_credit_accounts_response)
id_credit_account = create_credit_accounts_response.account.id

get_account_request = GetAccountsRequest(user_id=str(create_user_response_id))
get_account_response: GetAccountsResponse = accounts_gateway_service.GetAccounts(get_account_request)
print('Get account response:', get_account_response)

