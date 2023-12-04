from core.base.dto import DTO
from core.base.validators.dto_validator import DTOValidator
from core.attribute.attribute_collection import AttributeCollection
from numpy import int64


class AttributeSet(DTO, DTOValidator):

    DATA_MAP = {
        'attribute_set_id': [int, type(None), int64],
        'name': [str],
        'attribute_collection': [AttributeCollection, type(None)]
    }

    REQUIRED = (
        'name',
    )

    attribute_set_id: int
    name: str
    attribute_collection: AttributeCollection = AttributeCollection()

    '''
    Set and validate data
    '''
    def __init__(self, data: dict):
        super().__init__(data)
        super()._validate()
