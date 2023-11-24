from base.dto import DTO
from base.validators.dto_validator import DTOValidator
from numpy import int64


class Attribute(DTO, DTOValidator):

    DATA_MAP = {
        'attribute_id': [int, type(None), int64],
        'name': [str],
        'attribute_type': [str],
        'source_model': [str, type(None)],
    }

    REQUIRED = (
        'name',
        'attribute_type'
    )

    attribute_id: int = None
    name: str
    attribute_type: str
    source_model: str = None

    def __init__(self, data: dict):
        super().__init__(data)
        super()._validate()
