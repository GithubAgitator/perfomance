from pydantic import BaseModel

class DocumentSchema(BaseModel):
    """Описание структуры получения ответа документа"""
    url: str
    document: str

class GetDocumentTariffResponseSchema(BaseModel):
    tariff: DocumentSchema

class GetDocumentContractResponseSchema(BaseModel):
    contract: DocumentSchema