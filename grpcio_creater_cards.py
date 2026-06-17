import grpc
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import IssueVirtualCardRequest, IssueVirtualCardResponse
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardRequest, IssuePhysicalCardResponse
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub
from grpcio_get_user import create_user_response_id
from grpcio_get_account import id_credit_account

channel = grpc.insecure_channel("localhost:9003")

# Создаём gRPC-клиент для UsersGatewayService
cards_gateway_service = CardsGatewayServiceStub(channel)

# Формируем запрос на создание виртуальной карты
create_cards_virtual_request = IssueVirtualCardRequest(
    user_id=create_user_response_id,
    account_id=id_credit_account
)

# Отправляем запрос и получаем ответ
create_cards_virtual_response: IssueVirtualCardResponse = cards_gateway_service.IssueVirtualCard(create_cards_virtual_request)
print('Create cards virtual response:', create_cards_virtual_response)

# Формируем запрос на получение карты по ID, полученному из предыдущего ответа
get_cards_virtual_request_id =create_cards_virtual_response.card.id
print(get_cards_virtual_request_id)


# Формируем запрос на создание физической карты
create_cards_physical_request = IssuePhysicalCardRequest(
    user_id=create_user_response_id,
    account_id=id_credit_account
)

# Отправляем запрос и получаем ответ
create_cards_physical_response: IssuePhysicalCardResponse = cards_gateway_service.IssuePhysicalCard(create_cards_physical_request)
print('Create cards physical response:', create_cards_physical_response)

# Формируем запрос на получение карты по ID, полученному из предыдущего ответа
get_cards_physical_request_id = create_cards_physical_response.card.id
print(get_cards_physical_request_id)


