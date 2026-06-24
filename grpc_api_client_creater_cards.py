from clients.grpc.gateway.cards.client import build_cards_gateway_grpc_client
from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client



users_gateway_client = build_users_gateway_grpc_client()

create_user_response = users_gateway_client.create_user()
print(create_user_response)
user_id = create_user_response.user.id

account_gateway_client = build_accounts_gateway_grpc_client()
create_account_credit_response = account_gateway_client.open_credit_card(user_id)
print(create_account_credit_response)
account_id = create_account_credit_response.account.id
print(account_id)

cards_gateway_client = build_cards_gateway_grpc_client()
create_cards_issue_virtual = cards_gateway_client.issue_virtual_card(user_id, account_id)
cards_issue_virtua_id = create_cards_issue_virtual.card.id
print(create_cards_issue_virtual)

create_cards_physical_virtual = cards_gateway_client.issue_physical_card(user_id, account_id)
print(create_cards_physical_virtual)

