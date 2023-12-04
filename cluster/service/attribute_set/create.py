from core.attribute.attribute_set_repository import AttributeSetRepository


def execute(attribute_set_data: dict) -> dict:
    attribute_set_repository = AttributeSetRepository()
    attribute = attribute_set_repository.create(attribute_set_data)
    attribute_set_repository.save(attribute)
    attribute = attribute_set_repository.get_by_name(attribute_set_data['name'])
    return {"attribute_set_id": int(attribute.attribute_set_id)}
