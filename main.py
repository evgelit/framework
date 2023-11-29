from entity.entity_repository import EntityRepository
from base.search_criteria import SearchCriteria
from pprint import pprint

entity_repository = EntityRepository()

search_criteria = SearchCriteria([
    {"field": "last_name", "value": "Doe", "condition": "eq"},
])

collection = entity_repository.get_list(search_criteria)

for entity in collection:
    pprint(entity.to_dict())
