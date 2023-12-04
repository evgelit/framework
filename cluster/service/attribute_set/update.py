from core.attribute.attribute_set_repository import AttributeSetRepository


def execute(update_attribute_set_data: dict) -> None:
    attribute_set_repository = AttributeSetRepository()
    attribute_set = attribute_set_repository.get(update_attribute_set_data['attribute_set_id'])
    attribute_set.name = update_attribute_set_data['name']
    attribute_set_repository.save(attribute_set)
