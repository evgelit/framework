from core.attribute.attribute_repository import AttributeRepository


def execute(delete_attribute_data: dict) -> None:
    attribute_repository = AttributeRepository()
    attribute_repository.delete(delete_attribute_data["attribute_id"])
