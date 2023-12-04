from core.attribute.attribute_repository import AttributeRepository


def execute(attribute_data: dict) -> dict:
    attribute_repository = AttributeRepository()
    attribute = attribute_repository.create(attribute_data)
    attribute_repository.save(attribute)
    attribute = attribute_repository.get_by_name(attribute_data['name'])
    return {"attribute_id": int(attribute.attribute_id)}
