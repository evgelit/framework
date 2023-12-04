from core.entity.entity_repository import EntityRepository


def execute(update_entity_data: dict) -> None:
    entity_repository = EntityRepository()
    entity = entity_repository.get(update_entity_data['entity_id'])
    entity.entity_type = update_entity_data['entity_type']
    entity.attribute_set_id = update_entity_data['attribute_set_id']
    entity.attributes = update_entity_data['attributes']
    entity_repository.save(entity)
