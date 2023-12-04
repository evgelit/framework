from core.entity.entity_repository import EntityRepository


def execute(delete_entity_data: dict) -> None:
    attribute_repository = EntityRepository()
    attribute_repository.delete(delete_entity_data["entity_id"])
