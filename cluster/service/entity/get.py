from core.entity.entity_repository import EntityRepository
from core.base.search_criteria import SearchCriteria


def execute(filters: list = None) -> dict:
    repository = EntityRepository()
    result = {}
    if filters is None:
        search_criteria = SearchCriteria([])
    else:
        search_criteria = SearchCriteria(filters)
    entity_collection = repository.get_list(
        search_criteria
    )
    for entity in entity_collection:
        print(entity.to_dict())
        entity.entity_id = int(entity.entity_id)
        result[entity.entity_id] = entity.to_dict()
    return result
