from core.entity.entity_repository import EntityRepository


def execute(entity_data: dict) -> dict:
    entity_repository = EntityRepository()
    entity = entity_repository.create(entity_data)
    entity_repository.save(entity)
    attribute = entity_repository.get(attribute_data['name'])
    return {"attribute_id": int(attribute.attribute_id)}
