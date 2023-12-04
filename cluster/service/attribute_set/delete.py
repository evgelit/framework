from core.attribute.attribute_set_repository import AttributeSetRepository


def execute(delete_attribute_set_data: dict) -> None:
    attribute_set_repository = AttributeSetRepository()
    attribute_set_repository.delete(delete_attribute_set_data["attribute_set_id"])
