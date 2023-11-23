from base.dto import DTO
from base.validators.dto_validator import DTOValidator


class Attribute(DTO, DTOValidator):

    DATA_MAP = {
        'attribute_id': [int],
        'name': [str],
        'attribute_type': [str],
        'source_model': [str, type(None)],
    }

    REQUIRED = (
        'name',
        'attribute_type'
    )

    attribute_id: int
    name: str
    attribute_type: str
    source_model: str = None

    def __init__(self, data: dict):
        super().__init__(data)
        super()._validate()
