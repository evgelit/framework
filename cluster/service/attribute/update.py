from core.attribute.attribute_repository import AttributeRepository


def execute(update_attribute_data: dict) -> None:
    attribute_repository = AttributeRepository()
    attribute = attribute_repository.get(update_attribute_data['attribute_id'])
    attribute.name = update_attribute_data['name']
    attribute.attribute_type = update_attribute_data['attribute_type']
    attribute.source_model = update_attribute_data['source_model']
    attribute_repository.save(attribute)
