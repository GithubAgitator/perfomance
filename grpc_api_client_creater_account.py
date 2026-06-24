from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.users.client import build_users_gateway_grpc_client



users_gateway_client = build_users_gateway_grpc_client()

create_user_response = users_gateway_client.create_user()
print(create_user_response)
user_id = create_user_response.user.id
print(user_id)

account_gateway_client = build_accounts_gateway_grpc_client()

create_account_deposit_response = account_gateway_client.open_deposit_card(user_id)
print(create_account_deposit_response)
account_id = create_account_deposit_response.account.id
print(account_id)

get_account = account_gateway_client.get_accounts(user_id)
print(get_account)

create_account_savings_response = account_gateway_client.open_savings_card(user_id)
print(create_account_savings_response)

create_account_debit_response = account_gateway_client.open_debit_card(user_id)
print(create_account_debit_response)

create_account_credit_response = account_gateway_client.open_credit_card(user_id)
print(create_account_credit_response)
