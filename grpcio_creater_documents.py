import grpc
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import GetContractDocumentRequest, GetContractDocumentResponse
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import GetTariffDocumentRequest, GetTariffDocumentResponse
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from grpcio_get_account import id_credit_account

channel = grpc.insecure_channel("localhost:9003")

# Создаём gRPC-клиент для UsersGatewayService
documents_gateway_service = DocumentsGatewayServiceStub(channel)

# Формируем запрос на получение пользователя по ID, полученному из предыдущего ответа
get_tariff_request = GetTariffDocumentRequest(account_id=id_credit_account)

# Отправляем запрос и получаем ответ
get_tariff_response: GetTariffDocumentResponse = documents_gateway_service.GetTariffDocument(get_tariff_request)
print('Get tariff response:', get_tariff_response)

get_contract_document_request =GetContractDocumentRequest(account_id=id_credit_account)

# Отправляем запрос и получаем ответ
get_contract_document_response: GetContractDocumentResponse = documents_gateway_service.GetContractDocument(get_contract_document_request)
print('Get contract document response:', get_contract_document_response)