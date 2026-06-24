from clients.grpc.client import GRPCClient
from grpc import Channel
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import GetContractDocumentRequest, GetContractDocumentResponse
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import GetTariffDocumentRequest, GetTariffDocumentResponse
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub

class DocumetsGatewayGRPCClient(GRPCClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = DocumentsGatewayServiceStub(channel)

    def get_documents_tariff_api(self, request: GetTariffDocumentRequest) -> GetTariffDocumentResponse:
        return self.stub.GetTariffDocument(request)

    def get_documents_tariff(self, account_id: str) -> GetTariffDocumentResponse:
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_documents_tariff_api(request)

    def get_documents_contract_api(self, request: GetContractDocumentRequest) -> GetContractDocumentResponse:
        return self.stub.GetContractDocument(request)

    def get_documents_contract(self, account_id: str) -> GetContractDocumentResponse:
        request = GetContractDocumentRequest(account_id=account_id)
        return self.get_documents_contract_api(request)



def build_documents_gateway_grpc_client() -> DocumetsGatewayGRPCClient:
    return DocumetsGatewayGRPCClient(channel=build_gateway_grpc_client())