from core.attribute.attribute_set_repository import AttributeSetRepository
from core.attribute.attribute_repository import AttributeRepository


def execute(link_attribute_set_data: dict) -> None:
    attribute_set_repository = AttributeSetRepository()
    attribute_repository = AttributeRepository()
    attribute_set = attribute_set_repository.get(link_attribute_set_data['attribute_set_id'])
    attribute = attribute_repository.get(link_attribute_set_data['attribute_id'])
    attribute_set_repository.add_to_set(attribute_set, attribute)
