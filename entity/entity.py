from base.dto import DTO
from base.validators.dto_validator import DTOValidator
from numpy import int64


class Entity(DTO, DTOValidator):

    DATA_MAP = {
        'entity_id': [int, str, int64],
        'attribute_set_id': [int, str, int64],
        'entity_type': [str],
        'attributes': [dict],
    }

    REQUIRED = (
        'attribute_set_id',
        'entity_type'
    )

    entity_id: int or str = None
    entity_type: str = "default"
    attribute_set_id: int = None
    attributes: {}

    '''
    Set data
    '''
    def __init__(self, data: dict):
        super().__init__(data)
        super()._validate()
